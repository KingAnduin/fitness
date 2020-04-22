from rest_framework.pagination import PageNumberPagination


class PageSetting(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 5
    # 获取url参数中设置的每页显示数据条数
    page_size_query_param = 'size'
    # 获取url中传入的页码key
    page_query_param = 'page'

    # 计算总页数
    def cal_total_page(self, total_count):
        if total_count % self.page_size == 0:
            total_page = total_count // self.page_size
        else:
            total_page = total_count // self.page_size + 1
        return total_page