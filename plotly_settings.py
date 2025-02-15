import plotly.graph_objects as go
import config



def plotly_settings():
    data = config.GENRES_DICT

    sorted_items = sorted(data.items(), key=lambda x: x[1]['price'])

    categories = [item[0] for item in sorted_items]
    count_values = [item[1]['count'] for item in sorted_items]
    price_values = [item[1]['price'] for item in sorted_items]

    fig = go.Figure(data=[
        go.Bar(y=categories, x=count_values, name='Sum of games by tags', marker=dict(color='#7a73c0'), orientation='h'),
        go.Bar(y=categories, x=price_values, name='Total revenue, $', marker=dict(color='#3ebe9d'), orientation='h')
    ])

    fig.update_layout(
        title="Popular Steam Tags. Total revenue by tags",
        yaxis_title="Popular Tags",
        xaxis_title="Values",
        barmode='group',
        showlegend=True,
        template="plotly_dark"
    )

    fig.show()
