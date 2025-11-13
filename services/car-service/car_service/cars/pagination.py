from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ApiPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "size"
    page_size = 10
    max_page_size = 100

    # входной page — 0-based как в схеме; PageNumberPagination — 1-based.
    def get_page_number(self, request, paginator):
        raw = request.query_params.get(self.page_query_param, None)
        if raw is None:
            return 1
        try:
            page0 = int(raw)
        except Exception:
            return 1
        return max(1, page0 + 1)

    def get_paginated_response(self, data):
        # вернуть строго {page, pageSize, totalElements, items}
        page0 = (self.page.number - 1)
        return Response({
            "page": page0,
            "pageSize": self.get_page_size(self.request),
            "totalElements": self.page.paginator.count,
            "items": data,
        })
