import geopandas as gpd
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Read the mental health dataset
data_path = "/Users/Masih/Desktop/bootcamp /Project_3/Project-3-Group-6/mental_health.csv"
data = pd.read_csv(data_path)

# Group by 'Country' and calculate the mean of the 'Percent' column for each country
mean_percent_by_country = data.groupby('Country')['Percent '].mean().reset_index()

# Sort the DataFrame by the 'Percent' column in descending order
sorted_mean_percent_df = mean_percent_by_country.sort_values(by='Percent ', ascending=False)

# Load the world map GeoJSON data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the mental health data with GeoJSON data using a left join
merged_data = world.merge(sorted_mean_percent_df, how='left', left_on='name', right_on='Country')

# Fill missing values with zeros
merged_data['Percent '] = merged_data['Percent '].fillna(0)

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Mental Health Dashboard"),
    
    # Dropdown menu to select country
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in sorted_mean_percent_df['Country']],
        value=sorted_mean_percent_df.iloc[0]['Country'],  # Default value is the first country
        style={'width': '50%', 'margin-bottom': '20px'}
    ),
    
    # Bar plot
    dcc.Graph(id='bar-plot', style={'margin-bottom': '20px'}),
    
    # Choropleth map
    dcc.Graph(id='choropleth-map', style={'margin-top': '20px'}),
])

# Callback to update bar plot and choropleth map based on selected country
@app.callback(
    [Output('bar-plot', 'figure'),
     Output('choropleth-map', 'figure')],
    [Input('country-dropdown', 'value')]
)
def update_plots(selected_country):
    # Filter data for the selected country
    filtered_data = data[data['Country'] == selected_country]
    
    # Update bar plot
    bar_fig = px.bar(filtered_data, x='Year', y='Percent ', 
                     title=f'Mental Health Trend in {selected_country}',
                     labels={'Percent ': 'Mean Percent'})
    bar_fig.update_xaxes(title='Year')
    bar_fig.update_yaxes(title='Mean Percent')
    
    # Update choropleth map
    choropleth_fig = px.choropleth(merged_data, 
                                    geojson=merged_data.geometry, 
                                    locations=merged_data.index, 
                                    color='Percent ', 
                                    color_continuous_scale='OrRd',
                                    range_color=(0, merged_data['Percent '].max()),
                                    hover_name='name',
                                    labels={'Percent ': 'Mental Health Percent'}
                                   )
    choropleth_fig.update_geos(showcountries=True, countrycolor="Black", showcoastlines=True)
    choropleth_fig.update_layout(title_text="<b>Average Mental Health Issues by Country from 1990 to 2019</b>")
    choropleth_fig.update_layout(coloraxis_colorbar=dict(title='<b>Mental Health Percent (%)</b>',
                                                          ticks='outside',
                                                          tickvals=[0, merged_data['Percent '].max()],
                                                          ticktext=['Low', 'High'],
                                                          len=0.5,
                                                          thickness=15,
                                                          title_font={'size': 16},
                                                          tickfont={'size': 14}))
    choropleth_fig.update_geos(fitbounds="locations", visible=False)
    choropleth_fig.update_traces(marker_line_width=0.2, selector=dict(type='choropleth'))
    
    return bar_fig, choropleth_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
