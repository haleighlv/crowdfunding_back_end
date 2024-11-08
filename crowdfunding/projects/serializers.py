from rest_framework import serializers
from django.apps import apps


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source="supporter_id")

    class Meta:
        model = apps.get_model("projects.Pledge")
        fields = "__all__"
        
    def to_representation(self, instance):
        # instance is a Pledge (printing out type(instance))
        print('instance', instance, type(instance))
        # please run all the code from django rest framework that you would have run
        # if I didn't make my own to_representation method
        representation = super().to_representation(instance)
        print('representation', representation)
        
        if instance.anonymous:
            # Remove the supporter field if anonymous is True
            # representation is the JSON
            # representation.pop('supporter')
            del representation['supporter']
        return representation


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner_id")
    pledge_sum = serializers.ReadOnlyField(source="owner_id")
    

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

    class PledgeDetailSerializer(serializers.ModelSerializer):
        supporter = serializers.ReadOnlyField(source="supporter_id")
    class Meta:
        model = apps.get_model("projects.Pledge")
        fields = "__all__"
        read_only_fields = ["amount", "project"]

        def update(self, instance, validate_data):
            instance.comment = validate_data.get("comment", instance.comment)
            instance.anonymous = validate_data.get("anonymous", instance.anonymous)
            instance.supporter = validate_data.get("supporter", instance.supporter)
            instance.save()
            return instance