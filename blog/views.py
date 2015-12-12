from django.shortcuts import render

# first view

def post_list(request):
	return render(request, 'blog/post_list.html', {})

