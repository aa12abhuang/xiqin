from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect


class AuthMiddleware(MiddlewareMixin):
    """中间件1"""

    def process_request(self,request):
        # 需要排除不需要登录就能够访问的页面，不然会陷入死循环
        if request.path_info in ["/manage/login/"]:
            return
        # 如果没有返回值（返回null），继续；如果有返回值，如果有返回值 HttpResponse
        info = request.session.get("info")
        if info:
            return

        return redirect("/manage/login/")
