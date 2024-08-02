from rest_framework import serializers

from .models import Customer


class GenderChoiceSerializer(serializers.Field):
    def to_representation(self, value):
        gender_choices_dict = dict(Customer.GENDER_CHOICES)
        return gender_choices_dict.get(value, "Unknown")

    def to_internal_value(self, data):
        return data


class CustomerSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    gender = GenderChoiceSerializer()

    class Meta:
        model = Customer
        fields = (
            "id",
            "name",
            "gender",
            "age",
            "favorite_number",
            "created_at",
        )

    @staticmethod
    def get_created_at(obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
