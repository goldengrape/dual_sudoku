import flet as ft

class Number_card(ft.Draggable):
    def __init__(self,group="chess"):
        super().__init__(group=group,content=ft.ElevatedButton(
            width=50,height=50,
            text="9"))
        self.value=9
        self.color=None

nc1=Number_card()

def main(page: ft.Page):
    page.add(nc1)

if __name__ == "__main__":
    ft.app(target=main) 