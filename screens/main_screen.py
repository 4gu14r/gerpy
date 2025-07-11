from textual.screen import Screen
from textual.widgets import Header, Footer, Button
from textual.containers import Center
from textual.app import ComposeResult
from screens.form_screen import FormScreen

class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Center(Button("Iniciar", id="start_button"))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start_button":
            self.app.push_screen(FormScreen())

    def on_show(self) -> None:
        button = self.query_one("#start_button", Button)
        self.app.set_focus(button)