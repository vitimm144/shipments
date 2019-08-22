from rest_framework import viewsets
# import django_filters.rest_framework
from core.serializers import ShipmentSerializer
from core.models import Shipment


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    http_method_names = ["get", "post", "head", "put", "patch", "delete", "options"]
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    # filter_fields = ("shipment_code", "sender_name",)




