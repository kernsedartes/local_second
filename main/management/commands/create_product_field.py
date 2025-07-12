from django.core.management.base import BaseCommand
from integration_utils.bitrix24.bitrix_token import BitrixToken
import requests


class Command(BaseCommand):
    help = "Create product custom field in Bitrix"

    def handle(self, *args, **kwargs):
        webhook_url = "https://b24-68oetn.bitrix24.ru/rest/1/fo1yr9eyzzxghpvl/"
        method = "crm.product.property.add"
        fields = {
            "NAME": "Картинка товара",
            "CODE": "UF_CRM_PRODUCT_IMAGE",
            "PROPERTY_TYPE": "F",
            "MULTIPLE": "N",
            "MANDATORY": "N",
            "SHOW_FILTER": "Y",
            "SHOW_IN_LIST": "Y",
            "SORT": 100,
        }

        response = requests.post(
            webhook_url + method,
            json={"fields": fields},
        )
        data = response.json()
        if "error" in data:
            raise Exception(f"Bitrix error: {data}")

        self.stdout.write(self.style.SUCCESS(f"Created property: {data}"))
