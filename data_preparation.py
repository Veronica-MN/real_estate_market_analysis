import pandas as pd
import numpy as np

# data_preparation.py

def prepare_data(file_path):
    # Read pickled file
    data = pd.read_pickle(file_path)

    # Calculating age at purchase
    data['age_at_purchase'] = (data['date_sale'] - data['birth_date']).apply(lambda x: x.days) / 365
    data['age_at_purchase_rounded'] = data['age_at_purchase'].apply(lambda x: np.floor(x))
    data['age_interval'] = pd.cut(data['age_at_purchase'], bins=10, precision=0)

    # Grouping by age interval
    columns_of_interest = ['age_interval', 'sold']
    sold_by_age = data[columns_of_interest].groupby("age_interval").sum()

    # Creating price interval and grouping by price interval
    data['price_interval'] = pd.cut(data['price$'], bins=10)
    
    columns_of_interest = ['price_interval', 'sold']
    all_properties_by_price = data[columns_of_interest].groupby("price_interval").count()
    all_properties_by_price = all_properties_by_price.rename(columns={'sold': 'count'})

    sold_properties_by_price = data[columns_of_interest].groupby("price_interval").sum()
    all_properties_by_price['not_sold'] = all_properties_by_price['count'] - sold_properties_by_price['sold']
    all_properties_by_price['sold'] = sold_properties_by_price['sold']

    # Filtering sold properties and calculating correlations
    data_sold = data[(data['sold'] == 1) & (data['individual'] == 1)]
    covariance = np.cov(data_sold['age_at_purchase'], data_sold['price$'])
    correlation = np.corrcoef(data_sold['age_at_purchase'], data_sold['price$'])

    data_sold_no_na = data_sold.dropna()
    correlation_no_na = data_sold_no_na[['age_at_purchase', 'price$']].corr()

    return {
        'data': data,
        'sold_by_age': sold_by_age,
        'all_properties_by_price': all_properties_by_price,
        'sold_properties_by_price': sold_properties_by_price,
        'covariance': covariance,
        'correlation': correlation,
        'correlation_no_na': correlation_no_na,
    }