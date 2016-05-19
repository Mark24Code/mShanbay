import json
import copy
from django.http import JsonResponse,HttpResponse

def importtest():
	print('>>>>>>>>>>>>')
	print('import jsonresponse module success!')
	print('<<<<<<<<<<<<<')


class jsonResponse(object):
	"""增强jsonResponse"""
	def __init__(self):
		super(jsonResponse, self).__init__()
		self.data = {}
		self.errMsg = ""
		self.successMsg = ""
		self.code = ""

	def get_response(self):
		resp_data = {
			"data":self.data,
			"errMsg":self.errMsg,
			"successMsg":self.successMsg,
			"code":self.code
		}
		return JsonResponse(resp_data)


def creat_response(code):
	response = jsonResponse()
	response.code = code
	response.errMsg = ""
	if code == 200:
		response.successMsg = True
	response.data = {}
	return response


if __name__ == "__main__":
	test = creat_response(200)
	print('----Init-----')
	print('obj:',test)
	print('code:',test.code)
	print('----Dynamic---')
	test.errMsg = "Error"
	test.data = {'url':'/index/'}
	print('obj:',test)
	print('code:',test.code)
	print('errMsg:',test.errMsg)
	print('data:',test.data)



