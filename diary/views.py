from django.shortcuts import render
from .models import ColdEntry,Diary
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,get_list_or_404,redirect
from .forms import EntryForm,DiaryForm
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.


@login_required
def entryView(request,diary_pk):

    all_entries=ColdEntry.objects.filter(created_by=request.user,diary__pk=diary_pk).order_by("serial_no")
    
    return render(request,r'diary\entry.html',{"Entries":all_entries,"diary_pk":diary_pk})

@login_required
def updateEntry(request,rowId):
    responseData={}
    if request.method=='POST':
        
        entryToUpdate=get_object_or_404(ColdEntry,pk=rowId)

        updated=updateEntryField(entryToUpdate,request.POST)

        if updated:
            responseData['successfully_updated']=True

        else:
            responseData['successfully_updated']=False
            responseData['error']='Invalid data given'

    else:
        responseData['POST request is not allowed']    
    return JsonResponse(responseData)
    # currentObj=get_object_or_404(ColdEntry,serial_no=rowId)

    
    

def updateEntryField(entryObj,data):

    updated=True

    for fieldname,value in data.items():

        if fieldname=="serial_no":
            # Checking if the value is different or same
            if entryObj.serial_no!=int(value): 
                previousValue=entryObj.serial_no
                entryObj.serial_no=value
                entryObj.save()

                entries=ColdEntry.objects.filter(created_by=entryObj.created_by,serial_no=entryObj.serial_no)
                print(entries)
                if len(entries)>1:
                    entryObj.serial_no=previousValue
                    entryObj.save()

                    return False
                    


        elif fieldname=="packets":
            # Checking if the value is different or same
            if entryObj.packets!=int(value): 
                entryObj.packets=value

        elif fieldname=="rank":
            # Checking if the value is different or same
            if entryObj.rank!=str(value): 
                entryObj.rank=value
  
        elif fieldname=="floor":
            # Checking if the value is different or same
            # if values are not same then change

            if entryObj.floor!=str(value): 
                entryObj.floor=value

        elif fieldname=="removed_packets":
            # Checking if the value is different or same
            if entryObj.removed_packets!=str(value): 
                # if values are not same then change
                entryObj.removed_packets=value
        
        else:
            updated=False

        entryObj.save()

        # returning true becuase it's a POST request
        return updated
    
    
@login_required
def createEntry(request,diary_pk):

    responseData={}
    
    if request.method=='POST':
        form=EntryForm(request.POST)

        if form.is_valid():
            
            diary=get_object_or_404(Diary,pk=diary_pk)

            newEntryObj=form.save(commit=False)

            newEntryObj.created_by=request.user

            # Setting diary    
            newEntryObj.diary=diary

            newEntryObj.save()

            responseData['message']="Successfuly created"

            responseData['entryId']=newEntryObj.pk

            responseData['success']=True


        else:
            responseData['message']=form.errors
            responseData['success']=False


        return JsonResponse(responseData)


def deleteEntry(request,entryPk):
    responseData={}

    if request.method=='POST':

        entryObj=get_object_or_404(ColdEntry,pk=entryPk)
        entryObj.delete()

        responseData['deleted']=True

    else:
        responseData['deleted']=False

    return JsonResponse(responseData)

@login_required
def diariesView(request):

    diaries=Diary.objects.filter(user=request.user)

    return render(request,"diary/diaries.html",{"diaries":diaries})

def validate_serial(request,diary_pk):
    
    responseData={}
    serial_no=request.GET.get('serial_no','')

    currentDiaryObj=get_object_or_404(Diary,pk=diary_pk)

    try:
        get_list_or_404(ColdEntry,serial_no=int(serial_no),diary=currentDiaryObj)
        
        responseData['status']="Invalid serial_no"
        responseData['is_valid']=False
        
        print(responseData)

    except Exception as e:
        responseData['status']="Valid serial_no"
        responseData['is_valid']=True

    return JsonResponse(responseData)

@login_required
def newDiaryView(request):
    if request.method=='POST':
        form=DiaryForm(request.POST)
        
        if form.is_valid():

            diary_name=form.cleaned_data['diary_name']
            diary_year=int(datetime.date.today().year)

            diary_name=f"{diary_name}-{diary_year}"
            diaries=Diary.objects.filter(diary_name=diary_name,user=request.user)

            if(not diaries):
                diaryObj=form.save(commit=False)
                diaryObj.user=request.user
                diaryObj.year=int(datetime.date.today().year)

                diaryObj.save()
                
                return redirect('/')

            else:
                form.add_error("diary_name",'Diary name already exists')


    else:
        form=DiaryForm()
        
    
    return render(request,'diary/diarynew.html',{'form':form})
        