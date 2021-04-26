from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import RiskType, RiskTypeField
from .enums import FieldDataType


class RiskTypeTests(APITestCase):

    def setUp(self) -> None:
        property_risk = RiskType.objects.create(name="Property")
        auto_mobile_risk = RiskType.objects.create(name="Automobile")
        cyber_liablitiy_risk = RiskType.objects.create(name="Cyber Liability")

        risk_types = [property_risk, auto_mobile_risk, cyber_liablitiy_risk]

        for risk_type in risk_types:
            for ft_value in FieldDataType.values:
                RiskTypeField.objects.create(risk_type=risk_type, field_name=ft_value, field_type=ft_value)

        return super().setUp()

    def test_risktype_model_count(self):
        """
        Ensure model data is valid by count.
        """
        self.assertEqual(RiskType.objects.count(), 3)
        self.assertEqual(RiskTypeField.objects.count(), 12)

    def test_get_all_risktype(self):
        """
        Ensure we can risk types created.
        """
        url = reverse('risk:v1:risktype-list')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)

    def test_get_single_risktype(self):
        """
        Ensure we can get an expected risk type by id/pk.
        """
        property_risk = RiskType.objects.order_by('?').first()

        url = reverse('risk:v1:risktype-detail', kwargs={'pk': property_risk.id})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], property_risk.id)
        self.assertEqual(res.data['name'], property_risk.name)
        self.assertEqual(len(res.data['fields']), 4)
