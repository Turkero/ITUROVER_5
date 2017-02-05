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
			name5 = request.POST['name5']
			name6 = request.POST['name6']
			name7 = request.POST['name7']
			name8 = request.POST['name8']
			name9 = request.POST['name9']
			context={"form" : form,
					 "check" : True,
					 "name": name,
					 "name0": name0,
					 "name1": name1,
					 "name2": name2,
					 "name3": name3,
					 "name4": name4,
					 "name5": name5,
					 "name6": name6,
					 "name7": name7,
					 "name8": name8,
					 "name9": name9,
					 }
			return render(request, "base.html", context)
	else:
		context={"check" : False,}
		return render(request, "base.html", context)