from django.shortcuts import render
from pharmacy_bill.models import PharmacyBill
from payment.models import Payment,ClinicPay
from django.db.models import Count,Sum
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def cust_pdt_order_report(request):
    if request.method=="POST":
        sdate = request.POST.get('date')
        edate = request.POST.get('edate')

        sdate = datetime.strptime(str(sdate), '%Y-%m-%d')
        edate = datetime.strptime(str(edate), '%Y-%m-%d')

        if edate >= sdate:

            ob = Payment.objects.filter(date__range=(sdate, edate))
            # ob=orders.values('company_pdt__name').annotate(total_trans=Count('order_cp_id'),total_amount=Sum('amount'))
            print(ob)
            tot_amt=0
            for i in ob:
                print(i)
                tot_amt+=float(i.amount)
            d = datetime.today().date()
            sdate = sdate.date()
            edate = edate.date()
            context = {
                'x': ob,
                'amt': tot_amt,
                'date': d,
                'sdate': sdate,
                'edate': edate
            }
            # return render(request,'report/report2.html',context)
            template_path = 'report/report2.html'
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # find the template and render it.
            template = get_template(template_path)
            html = template.render(context)

            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            # if error then show some funny view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        else:
            message="End date mustbe greater than or same as start time "
            context={
                'msg':message
            }
            return render(request, 'report/select1.html',context)
    return render(request,'report/select1.html')

def pharmacy_report(request):
    if request.method=="POST":
        sdate = request.POST.get('date')
        edate = request.POST.get('edate')

        sdate = datetime.strptime(str(sdate), '%Y-%m-%d')
        edate = datetime.strptime(str(edate), '%Y-%m-%d')

        if edate >= sdate:

            ob = PharmacyBill.objects.filter(date__range=(sdate, edate))
            # ob=orders.values('company_pdt__name').annotate(total_trans=Count('order_cp_id'),total_amount=Sum('amount'))
            print(ob)
            tot_amt=0
            for i in ob:
                print(i)
                tot_amt+=float(i.amount)

            d = datetime.today().date()
            sdate = sdate.date()
            edate = edate.date()
            context = {
                'x': ob,
                'amt':tot_amt,
                'date': d,
                'sdate': sdate,
                'edate': edate
            }
            # return render(request,'report/report1.html',context)
            template_path = 'report/report1.html'
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # find the template and render it.
            template = get_template(template_path)
            html = template.render(context)

            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            # if error then show some funny view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        else:
            message="End date mustbe greater than or same as start time "
            context={
                'msg':message
            }
            return render(request, 'report/select1.html',context)
    return render(request,'report/select1.html')


def clinic_report(request):
    if request.method=="POST":
        sdate = request.POST.get('date')
        edate = request.POST.get('edate')

        sdate = datetime.strptime(str(sdate), '%Y-%m-%d')
        edate = datetime.strptime(str(edate), '%Y-%m-%d')

        if edate >= sdate:

            ob = ClinicPay.objects.filter(date__range=(sdate, edate))
            # ob=orders.values('company_pdt__name').annotate(total_trans=Count('order_cp_id'),total_amount=Sum('amount'))
            print(ob)
            tot_amt=0
            for i in ob:
                print(i)
                tot_amt+=float(i.amount)

            d = datetime.today().date()
            sdate = sdate.date()
            edate = edate.date()
            context = {
                'x': ob,
                'amt':tot_amt,
                'date': d,
                'sdate': sdate,
                'edate': edate
            }
            # return render(request,'report/report3.html',context)
            template_path = 'report/report3.html'
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # find the template and render it.
            template = get_template(template_path)
            html = template.render(context)

            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            # if error then show some funny view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        else:
            message="End date mustbe greater than or same as start time "
            context={
                'msg':message
            }
            return render(request, 'report/select1.html',context)
    return render(request,'report/select1.html')