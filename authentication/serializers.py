from rest_framework import serializers
from .models import CustomUser, Expense, ExpenseCategory
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if CustomUser.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists")
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be blank")
        user = self.context['request'].user
        if ExpenseCategory.objects.filter(user=user, name=value).exists():
            raise serializers.ValidationError("Category with this name already exists")
        return value
        
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number")
        return value

    def validate(self, data):
        if 'title' not in data:
            raise serializers.ValidationError("Title is required")
        if 'date' not in data:
            raise serializers.ValidationError("Date is required")
        if 'amount' not in data:
            raise serializers.ValidationError("Amount is required")
        if 'category' not in data:
            raise serializers.ValidationError("Category is required")
        return data