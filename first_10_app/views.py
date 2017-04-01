from django.shortcuts import render
from forms import MemberForm
# Create your views here.
def bemember(request):
	if request.POST:
		form = MemberForm(request.POST or None)
		if form.is_valid():
			form.save(commit = True)
			context={"check" : False,}
			return render(request, "eyv.html", context)
		else:
			print request.POST.get
			name = request.POST['name']
			name0 = request.POST['name0']
			name1 = request.POST['name1']
			name2 = request.POST['name2']
			name3 = request.POST['name3']
			name4 = request.POST['name4']
			context={"form" : form,
					 "check" : True,
					 "name": name,
					 "name0": name0,
					 "name1": name1,
					 "name2": name2,
					 "name3": name3,
					 "name4": name4,
					 }
			return render(request, "base2.html", context)
	else:
		context={"check" : False,}
		return render(request, "base2.html", context)