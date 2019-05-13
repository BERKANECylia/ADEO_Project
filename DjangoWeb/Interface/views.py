from django.shortcuts import render
from dataCRUD.models import *
from .scriptETL import *

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
    df_new=showMissingValues( PRG_STUDENT_SITE.pdobjects.all().to_dataframe() )

    df1_new=showMissingValues( ADR_STUDENTS.pdobjects.all().to_dataframe() )

    df2_new=showMissingValues( STUDENT_INTERNSHIP.pdobjects.all().to_dataframe() )

    context={'PRG_STUDENT_SITE':df_new.to_dict('split'),
             'ADR_STUDENTS':df1_new.to_dict('split'),
             'STUDENT_INTERNSHIP':df2_new.to_dict('split')
            }
    
    return render(request, 'etl.html', context)

def etl_mergetables(request):
    context=mergeTables(
        ADR_STUDENTS.pdobjects.all().to_dataframe() ,
        PRG_STUDENT_SITE.pdobjects.all().to_dataframe() ,
        STUDENT_INTERNSHIP.pdobjects.all().to_dataframe()
    )
    df=showMissingValues( mergedTables.pdobjects.all().to_dataframe() )
    context={'MERGEDTABLES':df.to_dict('split')
            }
    return render(request, 'etl_mergedtables.html', context)

def maps(request):
    return render(request, 'maps.html')