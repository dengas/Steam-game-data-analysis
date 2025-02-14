import plotly.graph_objects as go
import config



def plotly_settings():
    # Исходный словарь данных
    data = config.GENRES_DICT

    # Сортировка по количеству (от меньшего к большему)
    sorted_items = sorted(data.items(), key=lambda x: x[1]['price'])

    # Извлечение категорий, количества и цен из отсортированного списка
    categories = [item[0] for item in sorted_items]
    count_values = [item[1]['count'] for item in sorted_items]
    price_values = [item[1]['price'] for item in sorted_items]

    # Создание графика с горизонтальными барами
    fig = go.Figure(data=[
        go.Bar(y=categories, x=count_values, name='Количество игр, $', marker=dict(color='blue'), orientation='h'),
        go.Bar(y=categories, x=price_values, name='Общий доход', marker=dict(color='red'), orientation='h')
    ])

    # Настройка отображения
    fig.update_layout(
        title="Количество и цены по жанрам. Общий доход по жанрам",
        yaxis_title="Жанры",
        xaxis_title="Значения",
        barmode='group',
        showlegend=True,
        template="plotly_dark"
    )

    # Отображение графика
    fig.show()
