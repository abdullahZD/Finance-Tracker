from rest_framework import serializers
from .models import User, Category, Transaction

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


 #Category Serializer       
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


#Transaction Serializer
# serializers.py

class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(write_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'category_name', 'type', 'amount', 'date']

    def create(self, validated_data):
        category_name = validated_data.pop('category_name')
        user = self.context['request'].user

        # Fetch or create the category
        category, created = Category.objects.get_or_create(
            user=user, name=category_name, defaults={'default': False}
        )
        
        if not category.user and not created:
            category = Category.objects.create(
                user=user, name=category_name, default=False
            )

        validated_data['category'] = category
        return super().create(validated_data)
