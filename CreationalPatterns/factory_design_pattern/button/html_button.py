from button import Button


class HtmlButton(Button):

    def render(self):
        return ("HTML Button has been rendered")

    def on_click(self):
        return ("clicked HTML Button")