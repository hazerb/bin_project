from rest_framework import serializers
from binApp.models import BinOperation

class BinOperationSerializer(serializers.ModelSerializer):
	class Meta:
		model = BinOperation
		fields = ('operation', 'bin', 'collection_frequency')
