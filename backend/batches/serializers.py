from rest_framework import serializers
from .models import Batch


class BatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batch
        fields = "__all__"

    def validate_batch_name(self, value):
        return value.strip()