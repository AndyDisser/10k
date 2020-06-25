from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import TimestampForm
from .models import Timestamp
import datetime

# Create your views here.
def enterdata(request):
    form = TimestampForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("datacollection:viewdata")
    context = {
        "form" : form,
    }

    return render(request, 'datacollection/enterdata.html', context)

def viewdata(request):
    math = Timestamp.objects.filter(subject='AnNuMa')
    algo = Timestamp.objects.filter(subject='Algo1')
    pdb = Timestamp.objects.filter(subject="PDB")
    ppdc = Timestamp.objects.filter(subject="PPDC")
    rtks = Timestamp.objects.filter(subject="RTKS")
    kaggle = Timestamp.objects.filter(subject="Kaggle")
    edx = Timestamp.objects.filter(subject="edx")
    web = Timestamp.objects.filter(subject="WebProgramming")

    subj = []
    subjects = [math, algo, pdb, ppdc, rtks, kaggle, edx, web]
    for subject in subjects:
        subj.append([t.time_spend for t in subject])

    times = []
    for s in subj:
        try:
            sum = s[0]
            if len(s) > 1:
                for t in s[1:]:
                    sum += t
            times.append(sum)
        except Exception:
            sum = datetime.timedelta(0)
            times.append(sum)

    total_time = 0
    str_times = []
    for t in times:
        t = t.total_seconds()
        total_time += t
        hours = round(t // 60)
        minutes = round(t % 60)
        str_times.append(f'{hours}h {minutes}min')

    total_time = f"{round(total_time // 60)}h {round(total_time % 60)}min"
    print(f"\n\n{total_time}\n\n")

    context = {
        "AnNuMa" : str_times[0],
        "Algo1" : str_times[1],
        "PDB" : str_times[2],
        "PPDC" : str_times[3],
        "RTKS" : str_times[4],
        "Kaggle" : str_times[5],
        "edx" : str_times[6],
        "WebProgramming": str_times[7],
        "total_time": total_time
    }
    return render(request, 'datacollection/viewdata.html', context)
