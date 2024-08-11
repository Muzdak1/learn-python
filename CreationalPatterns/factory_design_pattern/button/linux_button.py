from button import Button


class LinuxButton(Button):

    def render(self):
        return ("Linux Button has been rendered")

    def on_click(self):
        return ("Clicked Linux Button")