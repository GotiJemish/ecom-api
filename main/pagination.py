from rest_framework import pagination
from rest_framework.response import Response



class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 10   # Default limit if not provided by frontend
    max_limit = 100      # Max limit to prevent abuse
    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'links':{
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                
            },
            'data': data,
            
            'limit': self.limit,
            'offset': self.offset,
        })




        # class CustomPagination(pagination.PageNumberPagination):
#     def get_paginated_response(self, data):
#         return Response({
#             'count': self.page.paginator.count,
#             'links':{
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link(),
                
#             },
#             'data': data,
            
#             'page_size': self.page_size,
#             'current_page': self.page.number,
#             'total_pages': self.page.paginator.num_pages,
#             'has_next': self.page.has_next(),
#             'has_previous': self.page.has_previous(),
#         })