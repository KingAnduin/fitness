from rest_framework.pagination import PageNumberPagination


class PageSetting(PageNumberPagination):
    # Ĭ��ÿҳ��ʾ����������
    page_size = 3
    # ��ȡurl���������õ�ÿҳ��ʾ��������
    page_size_query_param = 'size'
    # ��ȡurl�д����ҳ��key
    page_query_param = 'page'