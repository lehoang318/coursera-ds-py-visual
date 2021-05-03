# Import required packages
import pandas as pd
import plotly.express as px

# Read the airline data into pandas dataframe
#url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'
url = './airline_data.csv'

airline_data =  pd.read_csv(url,
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str,
                                   'Div2Airport': str, 'Div2TailNum': str})

# Overview
print('{}\nShape: {}\nHead\n{}'.format(url, airline_data.shape, airline_data.head(5)))

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
# fig.show()

# ### Let's start creating dash application
#
# #### Theme
#
# Proportion of distance group (250 mile distance interval group) by month (month indicated by numbers).
#
# #### To do:
#
# 1.  Import required libraries and create an application layout
# 2.  Add title to the dashboard using HTML H1 component
# 3.  Add a paragraph about the chart using HTML P component
# 4.  Add the pie chart created above using core graph component
# 5.  Run the app
#

# Import required libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
# from jupyter_dash import JupyterDash

# Needs to be run two times in a separate cell due to a jupyterdash bug
# JupyterDash.infer_jupyter_proxy_config()
# JupyterDash.infer_jupyter_proxy_config()

# Create a dash application
# app = JupyterDash(__name__)
print(__name__)
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard',
                                         style={'textAlign': 'center',
                                                'color': '#503D36',
                                                 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by month (month indicated by numbers).',
                                        style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig)])
if __name__ == '__main__':
    # app.run_server(mode="inline", host="localhost")
    app.run_server(debug=True)
