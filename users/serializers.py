# coding=utf-8
from __future__ import unicode_literals
import re
from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator
from .models import VerifyCode, Passwordreset, Advice
from tianyun_try1.settings import reg_email

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """

    # email = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'name', 'mobile', 'email', 'work_org', 'research_dir', 'last_login')
        read_only_fields = ('email',)


class AdviceSerializer(DynamicModelSerializer):
    class Meta:
        model = Advice
        fields = ('name', 'phone', 'email', 'advice')


class EmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)

    def validate_email(self, email):
        """
        验证邮箱是否注册
        """

        # 邮箱是否注册
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("用户邮箱已经存在")
        # 验证邮箱号码是否合法
        if not re.match(reg_email, email):
            raise serializers.ValidationError("邮箱号码非法")
        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, email=email).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return email


class UserRegSerializer(serializers.ModelSerializer):
    # code = serializers.CharField(required=True, write_only=True, max_length=6, min_length=6, label="验证码",
    #                              error_messages={
    #                                  "blank": "请输入验证码",
    #                                  "required": "请输入验证码",
    #                                  "max_length": "验证码格式错误",
    #                                  "min_length": "验证码格式错误"
    #                              },
    #                              help_text="验证码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    def validate_email(self, email):
        """
        验证邮箱是否注册
        """
        # 邮箱是否注册
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("用户邮箱已经存在")
        # 验证邮箱号码是否合法
        if not re.match(reg_email, email):
            raise serializers.ValidationError("邮箱号码非法")
        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, email=email).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")
        return email

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'mobile', 'work_org', 'research_dir', 'password')


class PasswordresetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=16,
                                     style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True
                                     )

    def validate_email(self, email):
        """
        验证邮箱是否注册
        """

        # 邮箱是否注册
        if User.objects.filter(email=email).count() == 0:
            raise serializers.ValidationError("请输入正确的邮箱")
        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, email=email).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return email

    def validate(self, attrs):
        del attrs["password"]
        return attrs

    class Meta:
        model = Passwordreset
        fields = ('email', 'password', 'add_time')
