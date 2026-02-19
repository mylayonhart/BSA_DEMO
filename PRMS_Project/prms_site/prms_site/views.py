from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Prescription, Prescriber, Account


def home(request):
    prescriptions = Prescription.objects.all()
    return render(request, "home.html", {
        "prescriptions": prescriptions
    })


def create_report(request):
    prescribers = Prescriber.objects.all()
    accounts = Account.objects.all()

    if request.method == "POST":
        md_code = request.POST.get("md_code")
        employee_id = request.POST.get("employee_id")
        rx_count = request.POST.get("rx_count")
        remarks = request.POST.get("remarks")

        prescriber = Prescriber.objects.get(md_code=md_code)
        account = Account.objects.get(employee_id=employee_id)

        Prescription.objects.create(
            md_code=prescriber,
            employee_id=account,
            date_time_created=timezone.now(),
            rx_count=rx_count,
            remarks=remarks
        )

        return redirect("home")

    return render(request, "create_report.html", {
        "prescribers": prescribers,
        "accounts": accounts
    })


def edit_report(request, report_id):
    report = get_object_or_404(Prescription, id=report_id)

    if request.method == "POST":
        report.rx_count = request.POST.get("rx_count")
        report.remarks = request.POST.get("remarks")
        report.save()
        return redirect("home")

    return render(request, "edit_report.html", {
        "report": report
    })


def delete_report(request, report_id):
    report = get_object_or_404(Prescription, id=report_id)
    report.delete()
    return redirect("home")
