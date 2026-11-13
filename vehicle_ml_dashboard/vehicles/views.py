import pandas as pd
from django.shortcuts import render
from .dashboard import frequency_table, high_value_cars, total_price_by_manufacturer

def dashboard_view(request):
    df = pd.read_csv("dummy_data/vehicles_data_1000.csv")
    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
        "high_value_cars": high_value_cars(df),
        "total_price": total_price_by_manufacturer(df),
    })