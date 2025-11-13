from rest_framework.pagination import PageNumberPagination

class ApiPagination(PageNumberPagination):
    page_query_param = "page"       # ?page=
    page_size_query_param = "size"  # ?size=
    page_size = 10                  # значение по умолчанию
    max_page_size = 100             # на всякий случай