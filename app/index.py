from textual.app import App
from screens.main_screen import MainScreen
from styles.app_tcss import APP_CSS


class MyApp(App):
    TITLE = "GerPy"
    CSS = APP_CSS

    def on_mount(self) -> None:
        self.push_screen(MainScreen())