from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import homework_message
from .serializers import homework_messageSerializer

# Create your views here.
@api_view(['GET'])
def messageAPI(request):
    message = "GET 요청 완료"
    return Response(message)
