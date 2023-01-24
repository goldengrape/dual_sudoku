import flet as ft
from sudoku_logic import * 
import random

global board
board=Board()
global current_piece
current_piece=Piece(0)

class Chess_Container(ft.DragTarget):
    def __init__(self,board,i):
        super().__init__(
            group="chess",
            content=ft.ElevatedButton(
                text=board.chesses[i].value,
                bgcolor=ft.colors.WHITE,
                width=50,height=50),
            on_accept=self.drug_accept)
        # self.chess=board.chesses[i]
        self.index=i
        self.row=board.chesses[i].row
        self.col=board.chesses[i].col
        self.value=board.chesses[i].value
        self.blockID=self.row//3*3+self.col//3
    @property
    def chess(self):
        return board.chesses[self.index]
    @chess.setter
    def chess(self,value):
        board.chesses[self.index]=value

    def drug_accept(self,e):
        print()
        print(f"row:{self.row},col:{self.col}")    
        print(f"before candidates:{board.chesses[self.index].candidates}")   
        # print(f"value {current_piece.value} in cadiates {board.chesses[self.index].candidates}:{current_piece.value in board.chesses[self.index].candidates}")
        board.put(current_piece,self.row,self.col) 
        print(f"after candidates:{board.chesses[self.index].candidates}")
        self.content.text=self.chess.value
        self.content.bgcolor= self.chess.color 
        self.update()
        block_container[self.blockID].content.bgcolor=board.block[self.row][self.col].color
        block_container[self.blockID].update()
        
def red_button_click(e):
    value=int(input_text.value) % 9
    print("value",value)
    number_card.content.text=str(value)
    number_card.content.color=ft.colors.RED
    number_card.update()
    current_piece.value=value
    current_piece.color="Red"

def blue_button_click(e):
    value=int(input_text.value) % 9
    number_card.content.text=str(value)
    number_card.content.color=ft.colors.BLUE
    number_card.update()
    current_piece.value=value
    current_piece.color="Blue"



input_text=ft.TextField(width=50,height=50)
red_button=ft.ElevatedButton(
            width=50,height=50,
            text="Red",icon="add",color=ft.colors.RED,
            on_click=red_button_click)
blue_button=ft.ElevatedButton(
            width=50,height=50,
            text="Blue",icon="add",color=ft.colors.BLUE,
            on_click=blue_button_click)



number_card=ft.Draggable(
            group="chess",
            content=ft.ElevatedButton(
            width=50,height=50,
            text=input_text.value))
input_group=ft.Column(controls=[
                ft.Row(controls=[input_text,red_button,blue_button],), 
                number_card])
chess_container=[Chess_Container(board,i) for i in range(81)]
chess_index_in_block={
    0:[0,1,2,9,10,11,18,19,20],
    1:[3,4,5,12,13,14,21,22,23],
    2:[6,7,8,15,16,17,24,25,26],
    3:[27,28,29,36,37,38,45,46,47],
    4:[30,31,32,39,40,41,48,49,50],
    5:[33,34,35,42,43,44,51,52,53],
    6:[54,55,56,63,64,65,72,73,74],
    7:[57,58,59,66,67,68,75,76,77],
    8:[60,61,62,69,70,71,78,79,80],
}
   

block_container=[
        ft.Row(width=(50+10)*3,
                height=(50+10)*3,
                    controls= [chess_container[c] for c in chess_index_in_block[i]],
                    wrap=True,
                    run_spacing=10,) 
        for i in range(9)]
board_container=ft.Row(
        width=((50+10)*3+10)*3 ,
        # controls=chess_container,
        controls=block_container,
        wrap=True,
        run_spacing=10,
        )

def main(page: ft.Page):
    def drag_accept(e):
        print("OK")
        page.update()

    page.add(
        ft.Row(
        controls=[board_container,input_group]))
ft.app(target=main, view=ft.WEB_BROWSER)