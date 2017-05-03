from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import View

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .constants import valid_data_types


# Create your views here.


class DisplayPage(View):
    """
    Simply displayes the page
    """
    template_name = 'stock_data.html'

    def get(self, request):
        return render(request, self.template_name)


class GainerLooserView(APIView):
    """
    The View which is hit by front end java script every x minute to get the gainer or loser data in json where x is defined
    in .js file.
    """
    def get(self, request):
        """
        The get api fetches data stored in cache

        :param request:
        :return:
        """
        class_name = self.__class__.__name__
        try:
            data_type = request.query_params['type'] # gainer or loser
            if not data_type in valid_data_types:
                raise Exception('Invalid data type requested')

            # tries to get data from the cache
            cache_data = cache.get(data_type)
            response = Response(data=cache_data, status=status.HTTP_200_OK)
            response['Access-Control-Allow-Origin'] = '*'
            return response
        except Exception as e:
            return Response(data=e.args or e.message, status=status.HTTP_400_BAD_REQUEST)
