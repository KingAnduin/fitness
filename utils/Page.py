from rest_framework.pagination import PageNumberPagination


class PageSetting(PageNumberPagination):
    # Ĭ��ÿҳ��ʾ����������
    page_size = 5
    # ��ȡurl���������õ�ÿҳ��ʾ��������
    page_size_query_param = 'size'
    # ��ȡurl�д����ҳ��key
    page_query_param = 'page'

    # ������ҳ��
    def cal_total_page(self, total_count):
        if total_count % self.page_size == 0:
            total_page = total_count // self.page_size
        else:
            total_page = total_count // self.page_size + 1
        return total_page