from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Batch
from .serializers import BatchSerializer
from permissions.permissions import IsAdmin


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [IsAuthenticated]
    
permission_classes = [
    IsAuthenticated,
    IsAdmin,
]