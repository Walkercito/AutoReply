"""Header text component with WhatsApp gradient effect."""

import reflex as rx
from AutoReply.styles.colors import dark_mode, gradients
from AutoReply.styles.style import apply_text_style, spacing

def header_text(size: str = "h2") -> rx.Component:
    """
    Renders the header text with WhatsApp gradient effect.
    
    Args:
        size: Text size style to apply (h1, h2, etc.)
        
    Returns:
        rx.Component: The styled header text component
    """
    return rx.box(
        rx.html(
            f"""
            <div style="display: inline-block; word-wrap: break-word; overflow-wrap: break-word; max-width: 100%;">
                <span style="color: {dark_mode['text']['default']}">Automatiza tus respuestas en </span>
                <span style="background: linear-gradient(90deg, #25D366 0%, #128C7E 100%); 
                      -webkit-background-clip: text; 
                      background-clip: text; 
                      -webkit-text-fill-color: transparent; 
                      color: transparent;">WhatsApp</span>
                <span style="color: {dark_mode['text']['default']}"> de manera sencilla</span>
            </div>
            """,
            style={
                **apply_text_style(size),
                "display": "block",
                "white_space": "normal",
                "width": "100%",
                "font_size": ["1.5rem", "1.8rem", "2.25rem", "2.5rem"],  # Responsive font size
                "line_height": ["1.75rem", "2rem", "2.5rem", "2.75rem"],  # Responsive line height
                "text_align": "left",
                "overflow_wrap": "break-word",
                "word_break": "break-word",
            }
        ),
        width="100%",
        overflow_x="hidden",
    )
