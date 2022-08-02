from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from binApp.models import BinOperation
from binApp.serializers import BinOperationSerializer


@csrf_exempt
def binApi(request):
	if request.method == 'GET':
		data = BinOperation.objects.all()
		bin_op_serializer = BinOperationSerializer(data, many=True)
		return JsonResponse(bin_op_serializer.data, safe=False)
	else:
		return JsonResponse("no post method", safe=False)
