APP_CSS = """
Screen {
    align: center middle;
    layout: vertical;
}

#formulario {
    width: 80%;
    max-width: 60;
    min-height: 20;
    max-height: 20;
    align: center middle;
    margin: 2 0;
    padding: 2;
    border: round yellow;
}

Input {
    width: 100%;
    border: round $secondary;
    margin: 1 0;
}

Static {
    text-align: center;
    margin-bottom: 1;
}

#botoes {
    padding-top: 1;
    layout: horizontal;
}

#botoes Button {
    width: 50%;
    margin: 0 0;
}

#botoes Button:first-child {
    margin-right: 1;
}
"""