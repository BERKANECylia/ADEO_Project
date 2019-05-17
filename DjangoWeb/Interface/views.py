from django.shortcuts import render
from dataCRUD.models import *
from .scriptETL import *
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

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
@user_passes_test(lambda u: u.is_superuser)
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
    context=mergeTables(
        ADR_STUDENTS.pdobjects.all().to_dataframe() ,
        PRG_STUDENT_SITE.pdobjects.all().to_dataframe() ,
        STUDENT_INTERNSHIP.pdobjects.all().to_dataframe()
    )
    df=showMissingValues( mergedTables.pdobjects.all().to_dataframe() )
    context={'MERGEDTABLES':df.to_dict('split')
            }
    return render(request, 'etl_mergedtables.html', context)

@login_required
def maps(request):
    return render(request, 'maps.html')

@login_required
def contact_us(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contacttemplate.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['induraj2020@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('home')

    return render(request, 'contact_us.html', {
        'form': form_class,
    })

#indu 17-may

def checking(request):
    #query_results= mergedTables.objects.all()
    #query_results=mergeTables.objects.filter(item=item).distinct('ID_ANO')
    #query_results= mergedTables.objects.raw('SELECT DISTINCT PRG FROM mergedTables')

    # .count()
    #context = {'query_results': query_results}

    df_new_prg = return_distinct_prg(mergedTables.pdobjects.all().to_dataframe())
    df_new_ville = return_distinct_ville(mergedTables.pdobjects.all().to_dataframe())
    df_new_cp = return_distinct_cp(mergedTables.pdobjects.all().to_dataframe())
    df_new_rem = return_distinct_rem(mergedTables.pdobjects.all().to_dataframe())
    df_new_year= return_distinct_year(mergedTables.pdobjects.all().to_dataframe())

    context = {'prg': df_new_prg,
               'ville': df_new_ville,
               'cp': df_new_cp,
               'rem': df_new_rem,
               'year':df_new_year,
               }


    return render(request,'checking.html',context)
    #return HttpResponse('<h1> hi </h1>')