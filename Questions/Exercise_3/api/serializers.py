from rest_framework import serializers
from Excercise_1.models import RoutorDetail


class RouterSerializer(serializers.ModelSerializer):
    sap_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RoutorDetail
        fields = '__all__'
