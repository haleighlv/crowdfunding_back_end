from rest_framework import serializers
from django.apps import apps
from django.contrib.auth import get_user_model
User = get_user_model()


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source="supporter_id")

    class Meta:
        model = apps.get_model("projects.Pledge")
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner_id")
    pledge_sum = serializers.ReadOnlyField(source="owner_id")
    
    def get_pledges_total(self, obj):
        pledges = obj.pledges.all()
        return
    

    class Meta:
        model = apps.get_model("projects.Project")
        fields = "__all__"



class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)


    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.goal = validated_data.get("goal", instance.goal)
        instance.image = validated_data.get("image", instance.image)
        instance.is_open = validated_data.get("is_open", instance.is_open)
        instance.data_created = validated_data.get("date_created", instance.date_created)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class DonationSerializer(serializers.ModelSerializer):
    supporter = UserSerializer(read_only=True)
    
    class Meta:
        model = apps.get_model("projects.Donation")
        fields = ['id', 'supporter', 'amount', 'comment', 'anonymous', 'project']