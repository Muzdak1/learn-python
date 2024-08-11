from button import Button


class WindowsButton(Button):

    def render(self):
        return ("Windows Button has been rendered")

    def on_click(self):
        return ("clicked Windows Button")