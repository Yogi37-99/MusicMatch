from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
# Create your views here.
def external(request):
	return render(request,'search.html')

def resultPage(request):
	inp = request.POST.get('param')
	inp1 = request.POST.get('param1')
	
	if(inp == None):
		return render(request,'search.html')
	elif(inp1 == None):
		out = run([sys.executable,'//home//nilesh015//Desktop//KMST_project//Django_Projects//testing//recommender_artist_var.py','10',inp],shell=False,stdout=PIPE)
	else:
		out = run([sys.executable,'//home//nilesh015//Desktop//KMST_project//Django_Projects//testing//recommender_artist_var.py','10',inp,inp1],shell=False,stdout=PIPE)
	s = out.stdout.decode()
	str1 = s.split('\n')
	strList = []
	artistList = []
	genreList = []
	for i in range(0,len(str1) - 1):
		temp = str1[i].split('...')
		temp1 = temp[3].rsplit('=',1)
		temp[3] = 'https://www.youtube.com/embed/' + str(temp1[1])
		strList.append(temp)
		artistList.append(temp[1])
		genreList.append(temp[2])

	artistSet = set(artistList)
	genreSet = set(genreList)

	if(len(strList) == 0):
		return render(request,'Error.html')	
	return render(request,'result.html',{'data1':strList,'aList':artistSet,'gList':genreSet})

def player(request):
	inp = request.GET.get('param1')
	#s = pk.decode()
	return render(request,'player.html',{'data1':inp})