import pandas as pd

df = pd.read_csv('Resources/cities.csv')
# save to html
df.to_html('data.html', index=False)