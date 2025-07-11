from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Input, Static
from textual.containers import Vertical, Horizontal
from textual.screen import Screen

class FormScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Vertical(
            Static("Preencha o formulário"),
            Input(placeholder="Nome", id="nome"),
            Input(placeholder="Email", id="email"),
            Horizontal(
                Button("Voltar", id="voltar"),
                Button("Gerar", id="gerar"),
                id="botoes"
            ),
            id="formulario"
        )

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "voltar":
            from screens.main_screen import MainScreen  # Importação tardia
            self.app.switch_screen(MainScreen())