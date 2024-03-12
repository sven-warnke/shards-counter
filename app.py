import streamlit.components.v1 as components


components.html(
    """
    <body>

    <input aria-label="Health" aria-invalid="false" aria-required="false" autocomplete="on" inputmode="text" name="" placeholder="" type="number" min="0" max="50" step="1" data-testid="stNumberInput-Input" value="50" style="background-color: green; color: red; font-size: 1000%; height:400px; width:400px; align: 'center';">

    <input aria-label="Health" aria-invalid="false" aria-required="false" autocomplete="on" inputmode="text" name="" placeholder="" type="number" min="0" max="30" step="1" data-testid="stNumberInput-Input" value="0" style="background-color: yellow; color: black; font-size: 1000%; height:400px; width:400px; align: 'center';">
    </body>
    """,
    scrolling=True,
    height=830,
    width=430,
)
