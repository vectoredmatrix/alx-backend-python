from rest_framework.pagination import PageNumberPagination



class LargeResultPagination(PageNumberPagination):
    
    page_size = 20
    page_size_query_param = "Page_size"
    max_page_size = 50