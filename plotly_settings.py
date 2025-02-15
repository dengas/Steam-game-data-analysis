import plotly.graph_objects as go
import config



def plotly_settings():
    data = config.GENRES_DICT

    sorted_items = sorted(data.items(), key=lambda x: x[1]['price'])

    categories = [item[0] for item in sorted_items]
    count_values = [item[1]['count'] for item in sorted_items]
    price_values = [item[1]['price'] for item in sorted_items]

    fig = go.Figure(data=[
        go.Bar(y=categories, x=count_values, name='Количество игр, $', marker=dict(color='blue'), orientation='h'),
        go.Bar(y=categories, x=price_values, name='Общий доход', marker=dict(color='red'), orientation='h')
    ])

    fig.update_layout(
        title="Количество игр и цены по жанрам. Общий доход по жанрам",
        yaxis_title="Популярные тэги",
        xaxis_title="Значения",
        barmode='group',
        showlegend=True,
        template="plotly_dark"
    )

    fig.show()
