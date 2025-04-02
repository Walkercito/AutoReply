"""Main application module for AutoReply."""

import reflex as rx
from AutoReply.pages.index import index
from AutoReply.styles.style import STYLESHEETS


app = rx.App(
    stylesheets=STYLESHEETS
)

app.add_page(
    component = index,
    route = "/",
    title = "AutoReply | Home",
    description = "Automatiza la atención a tus clientes de forma sencilla.",
)
