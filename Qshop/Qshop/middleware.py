from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from Qshop.settings import ERROR_PATH
import time
from CeleryTask.tasks import sendDing



class MiddleWareTest(MiddlewareMixin):
    def process_request(self,request):
        request_ip=request.META["REMOTE_ADDR"]
        if request_ip=="10.10.14.250":
            return HttpResponse('哈哈')
        print('我是process_request')

    def process_view(self,request,callback,callback_args,callback_kwargs):
        '''

        :param request:请求
        :param callback: 对应视图函数,访问哪个视图就是哪个视图函数
        :param callback_args: 视图函数的参数  元组类型
        :param callback_kwargs: 视图函数的参数  字典类型
        '''
        print("我是process_view")
        print(callback)

    def process_exception(self,request,exception):
        if exception:
            with open(ERROR_PATH,"a") as f:
                now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                content="[%s]:%s\n"%(now,exception)
                f.write(content)
                sendDing.delay(content)
            return HttpResponse("代码错误:<br> %s"%exception)

    def process_template_response(self,request,response):
        """
        必须返回一个render才可以触发
        :param response:
        :return:
        """
        print("我是process_templae_response")
        return HttpResponse("123")

    def process_response(self,request,response):
        """
        process_response 和 process_template_response 必须有返回值
        :param request:
        :param response:
        :return:
        """
        print("我是process_response")
        return response
