from django.shortcuts import render, HttpResponse


# Create your views here.
# log in
def log_in(request):
	if request.method == "POST":

		return

	# get 请求返回登录页面
	return render(request, 'myadmin/login/index.html')
