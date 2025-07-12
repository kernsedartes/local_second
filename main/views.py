import qrcode
from io import BytesIO
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import ProductLink
from .forms import GenerateQRForm
from django.conf import settings
from django.http import Http404
from integration_utils.bitrix24.bitrix_token import BitrixToken
import base64
import requests


@main_auth(on_start=True, set_cookie=True)
def home(request):
    try:
        app_settings = settings.APP_SETTINGS
        user_info = request.bitrix_user_token.call_api_method("user.current")
        user_name = f"{user_info['result']['NAME']} {user_info['result']['LAST_NAME']}"
    except Exception as e:
        user_name = "Unknown User"

    return render(request, "home.html", locals())


@main_auth(on_cookies=True)
def home_again(request):
    try:
        app_settings = settings.APP_SETTINGS
        user_info = request.bitrix_user_token.call_api_method("user.current")
        user_name = f"{user_info['result']['NAME']} {user_info['result']['LAST_NAME']}"
    except Exception as e:
        user_name = "Unknown User"

    return render(request, "home.html", locals())


def download_and_encode_image_from_field(image_field, bitrix_base_url):
    if not image_field:
        return None

    if isinstance(image_field, list) and image_field:
        download_url = image_field[0].get("value", {}).get("downloadUrl")
        if not download_url:
            return None

        full_url = f"{bitrix_base_url}{download_url}"

        response = requests.get(full_url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode("utf-8")

    return None


@main_auth(on_cookies=True)
def generate_qr(request):
    but = request.bitrix_user_token

    if request.method == "POST":
        form = GenerateQRForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data["product_id"]

            link = ProductLink.objects.filter(product_id=product_id).first()

            if not link:
                product_data = but.call_api_method(
                    "crm.product.get", {"id": product_id}
                ).get("result", {})

                image_field = product_data.get("PROPERTY_44") or product_data.get(
                    "PROPERTY_52"
                )

                bitrix_base_url = settings.BITRIX_BASE_URL

                image_base64 = download_and_encode_image_from_field(
                    image_field, bitrix_base_url
                )

                link = ProductLink.objects.create(
                    product_id=product_data.get("ID"),
                    name=product_data.get("NAME", ""),
                    description=product_data.get("DESCRIPTION", ""),
                    currency=product_data.get("CURRENCY_ID", ""),
                    price=product_data.get("PRICE", 0),
                    image_base64=image_base64,
                )

            url = request.build_absolute_uri(link.get_absolute_url())
            qr = qrcode.make(url)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            buffer.seek(0)

            filename = f"qr_{link.uuid}.png"
            file_path = default_storage.save(filename, ContentFile(buffer.read()))

            return render(
                request,
                "qr_result.html",
                {
                    "qr_url": default_storage.url(file_path),
                    "link": url,
                },
            )
    else:
        form = GenerateQRForm()

    return render(request, "generate_qr.html", {"form": form})


@main_auth(on_cookies=False)
def product_view(request, uuid):
    product = get_object_or_404(ProductLink, uuid=uuid)

    return render(request, "product_page.html", {"product": product})
