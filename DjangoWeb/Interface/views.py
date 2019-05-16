from django.shortcuts import render
from dataCRUD.models import *
from .scriptETL import *
from django.contrib.auth.decorators import login_required
from django.db.models import Max

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

# def descriptiveStats(request):
#     query_results=ProgramTable.objects.all()
#     context={'query_results':query_results}
#     return render(request, 'descriptiveStats.html', context)

@login_required
def descriptiveStats(request):
    # https://simpleisbetterthancomplex.com/tutorial/2016/12/06/how-to-create-group-by-queries.html
            #     City.objects.values('country__name') \
            # .annotate(country_population=Sum('population')) \
            # .order_by('-country_population')

    query_results=mergedTables.objects.all()
    # .count()
    context={'query_results':query_results}
    return render(request, 'descriptiveStats2.html', context)

@login_required
def etl(request):
    df_new=showMissingValues( PRG_STUDENT_SITE.pdobjects.all().to_dataframe() )

    df1_new=showMissingValues( ADR_STUDENTS.pdobjects.all().to_dataframe() )

    df2_new=showMissingValues( STUDENT_INTERNSHIP.pdobjects.all().to_dataframe() )

    context={'PRG_STUDENT_SITE':df_new.to_dict('split'),
             'ADR_STUDENTS':df1_new.to_dict('split'),
             'STUDENT_INTERNSHIP':df2_new.to_dict('split')
            }
    
    return render(request, 'etl.html', context)

@login_required
def etl_mergetables(request):    
    version=int(mergedTables.objects.all().aggregate(Max('idCSV'))['idCSV__max']) + 1
    description='Delete Null Values'
    ADR=redefineDFTypes(ADR_STUDENTS.pdobjects.all().to_dataframe())    
    PRG=redefineDFTypes(PRG_STUDENT_SITE.pdobjects.all().to_dataframe())
    STU=redefineDFTypes(STUDENT_INTERNSHIP.pdobjects.all().to_dataframe())
       
    df=mergeTables(ADR,PRG,STU)
    numberlines = df.ID_ANO.count()
    table = mergedTables.objects
    writeDF2Table(df, table, version, description )

    df=showMissingValues( mergedTables.pdobjects.filter(idCSV=version).to_dataframe() )
    context={'MERGEDTABLES' :df.to_dict('split') ,
             'NUMBERLINES'  :numberlines ,
             'VERSION'      :str(version) + " - " + description
            }
    return render(request, 'etl_mergedtables.html', context)

@login_required
def etl_mergetablesRF(request):    
    version=int(mergedTables.objects.all().aggregate(Max('idCSV'))['idCSV__max']) + 1
    description='Fill with RandomForest Algorithm'
    ADR=redefineDFTypes(ADR_STUDENTS.pdobjects.all().to_dataframe())    
    PRG=redefineDFTypes(PRG_STUDENT_SITE.pdobjects.all().to_dataframe())
    STU=redefineDFTypes(STUDENT_INTERNSHIP.pdobjects.all().to_dataframe())
       
    df=mergeTables(ADR,PRG,STU)
    numberlines = df.ID_ANO.count()
    table = mergedTables.objects
    writeDF2Table(df, table, version, description )

    df=showMissingValues( mergedTables.pdobjects.filter(idCSV=version).to_dataframe() )
    context={'MERGEDTABLES' :df.to_dict('split') ,
             'NUMBERLINES'  :numberlines ,
             'VERSION'      :str(version) + " - " + description
            }
    return render(request, 'etl_mergedtables.html', context)

@login_required
def maps(request):
    return render(request, 'maps.html')