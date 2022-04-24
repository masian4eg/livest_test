from rest_framework import serializers

from .models import CategoriesOfProducts, GroupsOfProducts, Products
from .utils import get_max_seq, set_seq, seq_plus


class Base(serializers.ModelSerializer):

    def create(self, validated_data):
        try:
            validated_data['seq']
        except KeyError:
            validated_data['seq'] = set_seq(self.Meta.model)
        if validated_data['seq'] <= get_max_seq(self.Meta.model):
            return seq_plus(self.Meta.model) in range(validated_data['seq'], get_max_seq(self.Meta.model))

        return super(Base, self).create(validated_data)


class CategoriesSerializer(Base):
    class Meta:
        model = CategoriesOfProducts
        fields = '__all__'


class GroupsSerializer(Base):
    class Meta:
        model = GroupsOfProducts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
