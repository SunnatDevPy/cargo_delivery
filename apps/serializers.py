from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from apps.models import Product, User


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserModelSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductModelSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['owner'] = UserModelSerializer(instance.owner, fields={"id", 'username', 'role'}).data
        return repr
