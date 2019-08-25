from rest_framework import viewsets
from core.serializers import ShipmentSerializer
from core.models import Shipment


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    http_method_names = ["get", "post", "head", "put", "patch", "delete", "options"]




