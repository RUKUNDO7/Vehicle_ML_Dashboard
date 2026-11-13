import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go
import pandas as pd

def frequency_table(df):
    # Simple counts
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

    # Convert to HTML
    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
    return table_html

def high_value_cars(df):
    return df[df['selling_price'] > 5000].to_html(classes="table table-bordered table-striped table-sm", index=False)

def total_price_by_manufacturer(df):
    return df.groupby(['manufacturer', 'transmission'])[['selling_price']].sum().to_html(classes="table table-bordered table-striped table-sm")