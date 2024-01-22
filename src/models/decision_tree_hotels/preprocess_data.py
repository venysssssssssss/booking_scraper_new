def preprocess_data(df):
    """
    Preprocess the data by removing symbols, converting columns to appropriate data types,
    and mapping categories to numbers.
    """
    df['price'] = df['price'].str.replace('US$', '').str.replace(',', '').astype(float)
    
    review_mapping = {
        'Good': 1,
        'Very Good': 2,
        'Wonderful': 3,
        'Review score': 4,
        'Excellent': 5,
        'Exceptional': 6,
    }
    df['avg review'] = df['avg review'].map(review_mapping)
    
    df['reviews count'] = df['reviews count'].str.replace(',', '').astype(float)
    
    return df