import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

#Creating DATA
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

##dcc.Graph() 안에서 id, figure 설정
app.layout = html.Div([dcc.Graph(id='scatterplot', ##id는 Reference를 위해 Define함
                    figure = dict(data=[
                                  go.Scatter(
                                  x=random_x,
                                  y=random_y,
                                  mode='markers',
                                  marker ={
                                    'size':12,
                                    'color':'rgb(51,204,153)',
                                    'symbol':'pentagon',
                                    'line':{'width':2}
                                  }
                                  )],
                                  layout=go.Layout(title="My Scatterplot",
                                                   xaxis = {'title':'Some X title'}))
                    ),
                    dcc.Graph(id='scatterplot2', ##id는 Reference를 위해 Define함
                                        figure = dict(data=[
                                                      go.Scatter(
                                                      x=random_x,
                                                      y=random_y,
                                                      mode='markers',
                                                      marker ={
                                                        'size':12,
                                                        'color':'rgb(200,204,53)',
                                                        'symbol':'pentagon',
                                                        'line':{'width':2}
                                                      }
                                                      )],
                                                      layout=go.Layout(title="Second plot",
                                                                       xaxis = {'title':'Some X title'}))
                    )])

if __name__ == '__main__':
    app.run_server()
