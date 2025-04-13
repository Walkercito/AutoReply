"""Background effects module for AutoReply application."""

import reflex as rx


def animated_background() -> rx.Component:
    """Create an animated background with grid overlay and light effects.
    
    Returns:
        rx.Component: A box component with animated background effects.
    """
    return rx.box(
        # Gradiente animado como fondo base
        rx.box(class_name="gradient-bg"),
        
        # Efectos de onda
        rx.box(class_name="wave-effect wave-effect-1"),
        rx.box(class_name="wave-effect wave-effect-2"),
        rx.box(class_name="wave-effect wave-effect-3"),
        
        # Puntos decorativos
        rx.box(class_name="dot-accent dot-accent-1"),
        rx.box(class_name="dot-accent dot-accent-2"),
        rx.box(class_name="dot-accent dot-accent-3"),
        
        # Grid overlay
        rx.box(class_name="grid-overlay"),
        class_name="animated-background",
    )