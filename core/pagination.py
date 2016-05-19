import json
import copy

class pagination(object):
    def __init__(self):
        super(pagination,self).__init__()



# def get_pageinfo(datas, pageSize=10,visiblePages = 6,currentPage=1):
#     totalPages = 0;
#     if (datas):
#         totalPages = len(datas)

#     pageinfo = {}

#     pageinfo["totalPages"] = totalPages
#     pageinfo["pageSize"] = pageSize
#     pageinfo["visiblePages"] = visiblePages
#     pageinfo["currentPage"] = currentPage
#     return pageinfo