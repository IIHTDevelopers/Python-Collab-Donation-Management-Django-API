from rest_framework.serializers import ModelSerializer
from .models import NGOModel,DonorModel,DonationModel,DonationRequestModel
class NGOSerializer(ModelSerializer):
    class Meta:
        model=NGOModel
        fields='__all__'

class DonorSerializer(ModelSerializer):
    class Meta:
        model=DonorModel
        fields='__all__'

class DonationSerializer(ModelSerializer):
    class Meta:
        model=DonationModel
        fields='__all__'

class DonationRequestSerializer(ModelSerializer):
    class Meta:
        model=DonationRequestModel
        fields='__all__'
