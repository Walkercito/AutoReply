import reflex as rx
from AutoReply.styles.colors import text_colors, background_colors, gradients, glass_effects, border_colors
from AutoReply.styles.style import container_styles, spacing, shadows, apply_text_style, apply_card_style
from AutoReply.components.header_text import header_text
from AutoReply.styles.font import font_sizes, font_weights

def header() -> rx.Component:
    header_container_style = {
        **container_styles["base"],
        "padding_y": spacing["10"],  # Padding vertical consistente
        "padding_x": spacing["5"],   # Padding horizontal consistente
        "min_height": "80vh",       # Altura razonable para la pantalla
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
        "width": "100%",
        "max_width": "100%",
    }
    
    # Estilo para el card con efecto glassmorphism
    glass_card_style = {
        **apply_card_style("base"),
        "background_color": glass_effects["card"]["background"],
        "backdrop_filter": glass_effects["card"]["backdrop_filter"],
        "border": f"1px solid {glass_effects['card']['border_color']}",
        "box_shadow": "0 15px 30px -5px rgba(0, 0, 0, 0.15), 0 10px 15px -6px rgba(0, 0, 0, 0.08)",  # Sombra más pronunciada
        "border_radius": "1rem",     # Bordes más redondeados
        "padding": spacing["6"],  # Padding consistente
        "width": "100%",            # Ocupa todo el ancho disponible
        "max_width": "95%",  # Ancho consistente
    }
    
    # Estilo para subtítulos
    subtitle_style = {
        **apply_text_style("body"),
        "color": text_colors["muted"],
        "margin_top": spacing["3"],      # Espacio consistente
        "margin_bottom": spacing["4"],   # Espacio consistente
        "font_size": font_sizes["lg"],    # Texto más grande
        "line_height": "1.6",            # Mejor espaciado entre líneas
        "max_width": "90%",              # Ancho consistente
        "font_weight": font_weights["medium"],  # Un poco más de peso visual
        "text_align": "center",          # Siempre centrado
    }
    
    # Estilos para botones
    button_style = {
        "background_color": background_colors["sand_dark"],
        "color": background_colors["sand_light"],
        "border_radius": "0.5rem",
        "padding_x": spacing["6"],
        "padding_y": spacing["3"],
        "font_weight": font_weights["medium"],
        "_hover": {
            "background_color": "rgba(44, 40, 36, 0.9)",
            "transform": "translateY(-2px)",
        }
    }
    
    # Estilo para botón secundario
    secondary_button_style = {
        "background_color": "transparent",
        "color": text_colors["default"],
        "border": f"1px solid {border_colors['default']}",  # Cambiamos 'subtle' por 'default' que sí existe
        "border_radius": "0.5rem",
        "padding_x": spacing["6"],
        "padding_y": spacing["3"],
        "font_weight": font_weights["medium"],
        "_hover": {
            "background_color": background_colors["subtle"],  # Aquí sí podemos usar 'subtle' porque existe en background_colors
            "transform": "translateY(-2px)",
        }
    }
    
    # Componente para modificar el header_text para hacerlo más grande
    # Vamos a usar directamente rx.heading para mayor control sobre el tamaño
    big_header = rx.box(
        rx.heading(
            "Automatiza tus respuestas en ", 
            rx.text.strong(
                "WhatsApp",
                background_image = gradients["success"],
                background_clip = "text",
                color = "transparent",
                font_weight = "bold"
            ),
            " de manera sencilla.",
            size="8",  # Tamaño extra grande consistente
            color = text_colors["default"],
            weight = "bold",
            z_index = "10",
            text_align = "center",
            line_height = "1.1",  # Línea más ajustada para que se vea mejor
            margin_bottom = "0",
        ),
        width="100%",
    )
    
    # Componente para el lado izquierdo (texto y botones)
    left_content = rx.box(
        big_header,  # Usamos nuestro header más grande personalizado
        rx.text(
            "Ahorra tiempo y responde al instante con nuestro sistema de respuestas automáticas impulsado por IA.",
            style=subtitle_style,
        ),
        rx.center(  # Centramos los botones horizontalmente
            rx.hstack(
                rx.button(
                    "Probar Gratis",
                    size="3",
                    style=button_style,
                ),
                rx.button(
                    "Ver Demo",
                    size="3",
                    style=secondary_button_style,
                ),
                spacing="4",
                wrap="wrap",  # Permitimos que los botones se envuelvan en pantallas muy pequeñas
            ),
            margin_top=spacing["6"],
            width="100%",
        ),
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",  # Centrado en todas las vistas
        width="100%",
        padding_x=spacing["2"],  # Padding mínimo
        text_align="center",  # Texto centrado en todas las vistas
    )
    
    # Componente para el lado derecho (card)
    right_content = rx.box(
        rx.box(
            rx.center(
                rx.text(
                    "📱",  # Emoji de teléfono
                    font_size="6em",  # Emoji más grande
                    opacity="0.7",
                ),
                rx.text(
                    "Respondiendo automáticamente",
                    color=text_colors["muted"],
                    font_size=font_sizes["base"],  # Texto más grande
                    margin_top=spacing["4"],
                ),
            ),
            style=glass_card_style,
            height="450px",  # Aumentamos aún más la altura
            display="flex",
            justify_content="center",
            align_items="center",
        ),
        display="flex",
        justify_content="center",  # Centrado en ambas vistas
        align_items="center",
        padding_x=spacing["4"],
        width="100%",
        margin_top=spacing["6"],  # Margen superior consistente
    )
    
    # Versión para escritorio (hstack - horizontal)
    desktop_layout = rx.desktop_only(
        rx.hstack(
            rx.box(
                left_content,
                width="50%",
            ),
            rx.box(
                right_content,
                width="50%",
            ),
            width="100%",
            justify_content="space-between",
            align_items="center",
            spacing="8",
        )
    )
    
    # Versión para tablet (hstack - horizontal con ajustes)
    tablet_layout = rx.tablet_only(
        rx.hstack(
            rx.box(
                left_content,
                width="50%",
            ),
            rx.box(
                right_content,
                width="50%",
            ),
            width="100%",
            justify_content="space-between",
            align_items="center",
            spacing="4",  # Menos espacio en tablet
        )
    )
    
    # Versión para móvil (vstack - vertical)
    mobile_layout = rx.mobile_only(
        rx.vstack(
            left_content,
            right_content,
            width="100%",
            justify_content="center",
            align_items="center",
            spacing="6",  # Espaciado consistente
            padding_x="0",  # Sin padding horizontal
        )
    )
    
    return rx.box(
        desktop_layout,
        tablet_layout,
        mobile_layout,
        width="100%",
        style=header_container_style,
        background_color="transparent",  # Cambiamos el fondo a transparente
    )