from django.shortcuts import render
from dataCRUD.models import *
from .scriptETL import showMissingValues

# Create your views here.
def home(request):
    return render(request, 'home.html')

# def descriptiveStats(request):
#     query_results=ProgramTable.objects.all()
#     context={'query_results':query_results}
#     return render(request, 'descriptiveStats.html', context)

def descriptiveStats(request):
    # https://simpleisbetterthancomplex.com/tutorial/2016/12/06/how-to-create-group-by-queries.html
            #     City.objects.values('country__name') \
            # .annotate(country_population=Sum('population')) \
            # .order_by('-country_population')

    query_results=mergedTables.objects.all()
    # .count()
    context={'query_results':query_results}
    return render(request, 'descriptiveStats2.html', context)

def etl(request):
    qs = PRG_STUDENT_SITE.pdobjects.all()
    df = qs.to_dataframe()
    df_new=showMissingValues(df)

    qs1 = ADR_STUDENTS.pdobjects.all()
    df1 = qs1.to_dataframe()
    df1_new=showMissingValues(df1)

    qs2 = STUDENT_INTERNSHIP.pdobjects.all()
    df2 = qs2.to_dataframe()
    df2_new=showMissingValues(df2)

    context={'PRG_STUDENT_SITE':df_new.to_dict('split'),
             'ADR_STUDENTS':df1_new.to_dict('split'),
             'STUDENT_INTERNSHIP':df2_new.to_dict('split')
            }
    print(context)
    return render(request, 'etl.html', context)

def maps(request):
    return render(request, 'maps.html')