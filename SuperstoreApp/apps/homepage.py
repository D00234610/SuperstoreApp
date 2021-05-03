#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

#to run the multipage app use the app import function

from app import app
#define the layout of the page
# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            #Header span the whole row
            #className: Often used with CSS to style elements with common properties.
            dbc.Col(html.H1("Superstore Sales Analysis", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='The Analysis is based on the sales and profit of items online. '
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='It consists of two pages: Page 1, which shows the sales and profit of the superstore from 2014 to 2017, '
                                     'Page 2, shows the city wise sales in the superstore.')
                    , className="mb-5")
        ]),

        dbc.Row([
            # 2 columns of width 6 with a border
            dbc.Col(dbc.Card(children=[html.H3(children='The superstore dataset used for the Analysis',
                                               className="text-center"),
                                       dbc.Button("Superstore Sales Data",
                                                  href="https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="green", outline=True)
                    , width=6, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access to the code used to build this dashboard',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://github.com/D00234610/SuperstoreApp",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="green", outline=True)
                    , width=6, className="mb-4"),

        ], className="mb-5"),
        html.A("The app provides insights on top selling and least selling products in the online market.")

    ])

])

# needed only if running this as a single page app
#if __name__ == '__main__':
#    app.run_server(port=8098,debug=True)

