#!/usr/bin/env python
# coding: utf-8

# In[32]:


#import packages to create app
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from app import app
import plotly.express as px
import pandas as pd
import numpy as np

store = pd.read_excel('C:/Users/devsu/Downloads/superstore.xls')
store.head()

#get unique continents
cont_names = store['State'].unique()
cols=list(store.columns)


# Create the dash app
#app = dash.Dash(__name__)
#change background and color text
colors = {
    #background to rgb(233, 238, 245)
    'background': '#000000',
    'text': '#ffffff'
}


layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1('Super Store Sales',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    #Add multiple line text 
    html.Div('''
        City Wise Sales in the US 
    ''', style={
        'textAlign': 'center',
        'color': colors['text']}
    ),

    html.Label('Select State'),
    dcc.Dropdown(id='state_dropdown',
                 options=[{'label': i, 'value': i}
                          for i in cont_names],
                 value=['Kentucky', 'California', 'Florida', 'North Carolina',
       'Washington', 'Texas', 'Wisconsin', 'Utah', 'Nebraska',
       'Pennsylvania', 'Illinois', 'Minnesota', 'Michigan', 'Delaware',
       'Indiana', 'New York', 'Arizona', 'Virginia', 'Tennessee',
       'Alabama', 'South Carolina', 'Oregon', 'Colorado', 'Iowa', 'Ohio',
       'Missouri', 'Oklahoma', 'New Mexico', 'Louisiana', 'Connecticut',
       'New Jersey', 'Massachusetts', 'Georgia', 'Nevada', 'Rhode Island',
       'Mississippi', 'Arkansas', 'Montana', 'New Hampshire', 'Maryland',
       'District of Columbia', 'Kansas', 'Vermont', 'Maine',
       'South Dakota', 'Idaho', 'North Dakota', 'Wyoming',
       'West Virginia'],
                 multi=True,
                style={'width':'70%'}
    ),

    dcc.Graph(
        id='Sales_Report'
    ),
])

@app.callback(
    Output(component_id='Sales_Report', component_property='figure'),
    Input(component_id='state_dropdown', component_property='value')
)
def update_graph(selected_cont):
    if not selected_cont:
        return dash.no_update
    data =[]
    for j in selected_cont:
            data.append(store[store['State'] == j])
    df = pd.DataFrame(np.concatenate(data), columns=cols)
    df=df.infer_objects()
    scat_fig = px.treemap(df,path=['State','City'], values='Sales')
    # Change the axis titles and add background colour using rgb syntax
    scat_fig.update_layout({'xaxis': {'title': {'text': 'Sales'}},
                  'yaxis': {'title': {'text': 'Profit'}}}, 
                  plot_bgcolor='rgb(0, 0, 0)',paper_bgcolor='rgb(0, 0, 0)', height=1000)

    return scat_fig



#if __name__ == '__main__':
 #   app.run_server(port=8098,debug=True)


# In[ ]:



