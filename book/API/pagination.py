from rest_framework.pagination import PageNumberPagination



class BookPagination(PageNumberPagination):
    page_size = 5
    #Page default parameter is 'page'
    page_query_param = 'pg'