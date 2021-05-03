#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import packages to create app
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output



import plotly.express as px
import pandas as pd
import numpy as np
from app import app

df = pd.read_excel('C:/Users/devsu/Downloads/superstore.xls')
df.head()

#get unique continents
cont_names = df['State'].unique()
cols=list(df.columns)


# Create the dash app
#app = dash.Dash(__name__)
#change background and color text
colors = {
    #background to rgb(255, 204, 255)
    'background': '#ffccff',
    'text': '#1c1cbd'
}
 
#add the layout for the page

layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1('SuperStore Sales Analysis',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    #Add multiple line text 
    html.Div('''
        Superstore sales in US from 2014 to 2017 
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
        id='Sales1'
    ),
    html.Div([
        html.Div([
            dcc.Graph(
                id='Superstore',
            )
        ],style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='Sales2',
            )
        ],style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
    ])

])

@app.callback(
    [Output(component_id='Sales1', component_property='figure'),
    Output(component_id='Sales2', component_property='figure'),
    Output(component_id='Superstore', component_property='figure')],
    Input(component_id='state_dropdown', component_property='value')
)
def update_graph(selected_cont):
    if not selected_cont:
        return dash.no_update
    data =[]
    for j in selected_cont:
            data.append(df[df['State'] == j])
    df1 = pd.DataFrame(np.concatenate(data), columns=cols)
    df1=df1.infer_objects()
    scat_fig = px.sunburst(df1,path=['Country','Category','Sub-Category'],
                 values='Sales',color='Category',
                 hover_data =['Sales','Quantity','Profit'])
    # Change the axis titles and add background colour using rgb syntax
    scat_fig.update_layout({'xaxis': {'title': {'text': 'Profit'}},
                  'yaxis': {'title': {'text': 'Sales'}}}, 
                  plot_bgcolor='rgb(255, 204, 255)',paper_bgcolor='rgb(255, 204, 255)',height=600,title_text='Product Categories & Sub-Categories'     )
    
    
    line_fig = px.scatter(df1, x='Profit',y='Sales' , color ='Category', hover_name='State', title='Sales & Profit by Region')
    line_fig.update_layout(plot_bgcolor='rgb(255, 204, 255)',
        paper_bgcolor='rgb(255, 204, 255)')

    fig = px.scatter(df1, x='Order Date', y='Sales',
                 color='Category', size='Sales', 
                 title='Superstore Daily Sales Analysis')
    fig.update_layout(plot_bgcolor='rgb(255, 204, 255)',paper_bgcolor='rgb(255, 204, 255)')
    return [scat_fig, line_fig, fig]



#if __name__ == '__main__':
 #   app.run_server(port=8095,debug=True)


# In[ ]:





# In[ ]:




