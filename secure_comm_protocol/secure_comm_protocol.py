"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    messages: list[str] = []  # Inicializa la lista de mensajes
    user_message: str = ""

    def send_message(self):
        """Envío de mensaje al chat."""
        if self.user_message.strip():  # No enviar mensajes vacíos
            self.messages.append(self.user_message)
            self.user_message = ""  # Limpiar el input

    def get_messages(self) -> list[str]:
        """Devuelve los mensajes actuales."""
        return self.messages
    
    def update_user_message(self, value: str):
        """Actualiza el mensaje del usuario."""
        self.user_message = value

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Bienvenido al Chat en Tiempo Real", size="2xl"),
            rx.text(
               "Conéctate y habla con otros en tiempo real. No se guarda ninguna información, todo es privado y temporal.",
            style={"fontSize": "18px", "marginTop": "20px"},
            ),
            rx.link(
                rx.button("Comenzar a chatear", on_click=lambda: rx.redirect("/chat"), style={"backgroundColor": "#4CAF50", "color": "white", "padding": "10px 20px", "borderRadius": "5px"}),
                style={"textAlign": "center", "padding": "50px"},
                #href="http://l127.0.0.1:3001/chat",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )



# Función para definir la interfaz del chat
@rx.page(route="/chat", title="Chat")
def chat_page():
    return rx.container(
        rx.heading("Chat en tiempo real"),
        rx.box(
            rx.foreach(State.messages, 
                       lambda msg: rx.text(msg)),
            id="chat_box",
            style={"height": "300px", "overflowY": "scroll", "border": "1px solid #ccc", "padding": "10px"}
        ),
        rx.input(
            on_change=State.update_user_message,
            value=State.user_message,
            placeholder="Escribe tu mensaje...",
            style={"width": "80%"}
        ),
        rx.button("Enviar", on_click=State.send_message, style={"width": "15%"}),
        style={"display": "flex", "flexDirection": "column", "gap": "10px", "alignItems": "center"}
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(chat_page, route="/chat")
