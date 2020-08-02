from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,'index.html')

def analyse(request):
	txt=request.POST.get('text','Try again')
	print(txt)
	rmpunc=request.POST.get('removepunc','off')
	uppercase=request.POST.get('ToUpper','off')
	Countlen=request.POST.get('countlen','off')
	Spaceremover=request.POST.get('removeextraspace','off')
	rmnewline=request.POST.get('removenewline','off')
	upfirstletter=request.POST.get('upfirstletter','off')
	analysed=txt
	purps=''
	if rmpunc=="on":
		result=""
		purps="Remove Punctuation, "	
		panctuation='''/(+-&_?!;:'."*')'''
		for char in txt:
			if char not in panctuation:
				result += char
			analysed=result
	if uppercase=='on':
		purps +="Convert To upper, "
		analysed=analysed.upper()
		
			
	if rmnewline=='on':
		purps +="Remove New Line, "
		result=''
		for char in analysed:
			if char != "\n" and char!="\r":
				result += char
		analysed=result
		
	if Spaceremover=='on':
		purps +='Remove Extra Spaces, '
		l=analysed.split()
		result=''
		for words in l:
			result += words +" "
		analysed=result
		
			
	if Countlen=='on':
		purps +="Count Number Of lines, "
		analysed=len(analysed)
	
	if upfirstletter=='on':
		purps +="Upper first letter of Word, "
		analysed=analysed.title()
	
		
	param={'purpose':purps,'text':analysed}
	return render(request,'analyse.html',param)
def about(request):
	return render(request,'about.html')
def contact(request):
	return render(request,'contact.html')