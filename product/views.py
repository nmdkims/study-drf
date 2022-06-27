from rest_framework.response import Response
from rest_framework.views import APIView

from product.serializers import EventSerializer
from rest_framework import status
from product.models import Event


class ProductView(APIView):

    def get(self, request):
        from datetime import datetime
        today = datetime.now().date()
        products = Event.objects.filter(
            exposure_start_date__lte=today,
            exposure_end_date__gte=today,
            is_active=True
        )

        return Response(EventSerializer(products, many=True).data, status=status.HTTP_200_OK)

    # 생성
    def post(self, request):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()

            return Response(event_serializer.data, status=status.HTTP_200_OK)

    # 수정
    def put(self, request, obj_id):
        product = Event.objects.get(id=obj_id)

        event_serializer = EventSerializer(product, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_200_OK)

        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
