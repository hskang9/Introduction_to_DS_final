import graphlab as gl
import numpy as np

# Load data
df = gl.SFrame.read_csv('../ids_final/ids_final/static/translated_and_cleaned_data2.csv')
df.rename({'\xef\xbb\xbfip': 'ip'})

# Pick elements which affects the clustering of the item
sf = df['ip','Continent', 'Country', 'City', 'travel date', 'Travel Period', 'Price', 'id']
qf = sf.to_dataframe().dropna()
del qf['ip']

def recommend(query):
    # Nation, City, travel period, travel date, or price
    loaded_model = gl.load_model('../ids_final/ids_final/static/recommend.model')
    columns = ['Continent', 'Country', 'City', 'travel date', 'Travel Period', 'Price']
    search = None
    query = list(map(lambda x : int(x) if x.isdigit() else x, query.split(', ')))

    for column in columns:
        filter = qf[qf[column].isin(query)]
        if len(filter.index) != 0:
            search = filter
    print(query)
    print(search)
    search_id = search['id'] #qf[mask]['id']


    # Recommend
    recom = loaded_model.get_similar_items([int(i) for i in search_id])
    dt=recom['similar']
    return qf.loc[dt]
