import json
import os
from django.conf import settings
from .models import Transport
from .serializers import TransportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import Cast
from django.db.models.fields import IntegerField, DecimalField



def load_trips():
    path = os.path.join(settings.BASE_DIR, 'data.json')
    with open(path, 'r', encoding='utf-8') as f:
        trips = json.load(f)

    for trip in trips['transport']:
        name = trip['name']
        price_confort = trip['price_confort']
        price_econ = trip['price_econ']
        city = trip['city']
        duration = trip['duration']
        seat = trip['seat']
        bed = trip['bed']

        Transport.objects.get_or_create(name=name, price_confort=price_confort, price_econ=price_econ, city=city,
                                        duration=duration, seat=seat, bed=bed)
    return


class TransportListView(APIView):
    def get(self, request):
        load_trips()
        queryset = Transport.objects.all()
        serializer_class = TransportSerializer(queryset, many=True)
        return Response(serializer_class.data)
        

    
class TransportFilterListView(APIView):
    def get(self, request, city, format=None):
        load_trips()
        transports = Transport.objects.filter(city=city)
        transports = transports.annotate(
            duration_as_int=Cast('duration', IntegerField()),
            price_econ_as_decimal=Cast('price_econ', DecimalField(max_digits=5, decimal_places=2))
        )
        fastest_transport = transports.order_by('duration_as_int').first()
        cheapest_transport = transports.order_by('price_econ_as_decimal').first()
        serializer_fastest = TransportSerializer(fastest_transport)
        serializer_cheapest = TransportSerializer(cheapest_transport)
        return Response({
            'fastest': serializer_fastest.data,
            'cheapest': serializer_cheapest.data
        })
