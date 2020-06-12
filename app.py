# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:16:44 2020

@author: KBold
"""


 #A minimal dash app should have the following: 
     #• app.py  is the main file that contains the code for the dash app 
     #• requirements.txt  contains the list of python packages that your app needs (so the web server can install them at the deployment stage) 
     #• runtime.txt contains the version of python needed to run the app 
     #• Procfile contains the instruction to run the web app
     
#File1: app.py
import flask; 
import plotly.express as px 
import dash; 
import dash_core_components as dcc; 
import dash_html_components as html 
from dash.dependencies import Input, Output

# Setup the app. The server & app names should match those in Procfile 
server = flask.Flask(__name__) 
app = dash.Dash(__name__, server=server) 
tips= px.data.tips(); fig = px.scatter(tips, x="total_bill", y="tip")
app.layout = html.Div([dcc.RadioItems(id="gender1", options=[{'label': 'Female', 'value': 'Female'}, 
                                                             {'label': 'Male', 'value': 'Male'}], value='Female'), dcc.Graph(id="fig1", figure=fig)])
@app.callback(Output('fig1', 'figure'),[Input('gender1', 'value')])
def updateGender(g):    return  px.scatter(tips.query("sex=='"+g+"'"), x="total_bill", y="tip")
if __name__ == '__main__': 
    app.server.run(debug=True, use_reloader=False) # Run the Dash app
    
    
# File2: requirements.txt
#• You can get a list of ALL packages currently installed in your python using 
# pip freeze > requirements.txt 
#However, for our example we only need: 
