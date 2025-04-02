"""Background effects module for AutoReply application."""

import reflex as rx


def animated_background() -> rx.Component:
    """Create an animated background with grid overlay and light effects.
    
    Returns:
        rx.Component: A box component with animated background effects.
    """
    return rx.box(
        rx.box(class_name="grid-overlay"),
        rx.box(class_name="light-effect light-effect-1"),
        rx.box(class_name="light-effect light-effect-2"),
        rx.box(class_name="light-effect light-effect-3"),
        class_name="animated-background"
    )