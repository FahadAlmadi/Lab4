from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Define the tax rate
tax_rate = 0.15  # 15%

@require_http_methods(["GET"])
def default_view(request):
    return HttpResponse("<h1>This is a site to calculate tax.</h1>")

@require_http_methods(["GET"])
def calculate_tax(request, number):
    try:
        number = float(number)
        total_price = number * (1 + tax_rate)
        return HttpResponse(f"<h1>Total Price After 15% Tax: ${total_price:.2f}</h1>")
    except ValueError:
        return HttpResponse("<h1>Invalid input. Please provide a valid number.</h1>")

@require_http_methods(["GET"])
def tax_rate_view(request):
    return render(request, "tax_calculation/tax_rate.html", {"tax_rate": tax_rate})
