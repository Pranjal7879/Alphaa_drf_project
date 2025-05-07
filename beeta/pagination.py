from rest_framework import pagination
from rest_framework.response import Response

class CustomProductPagination(pagination.PageNumberPagination):
    page_size = 5
    # page_size_query_param = 'page_size'
    # max_page_size = 50

    # def get_paginated_response(self, data):
    #     return Response(
    #         {
    #             'navigation':{
    #                 'next_page':self.get_next_link()
    #             }
    #         }
    #     )