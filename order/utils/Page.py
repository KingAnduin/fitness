from rest_framework.pagination import PageNumberPagination


class PageSetting(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 3
    # 获取url参数中设置的每页显示数据条数
    page_size_query_param = 'size'
    # 获取url中传入的页码key
    page_query_param = 'page'