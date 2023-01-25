import flet as ft
from sudoku_logic import * 
import random

global board
board=Board()
global current_piece
current_piece=Piece(0)
global chess_width,chess_height,spacing
chess_width=40
chess_height=40
spacing=5

class Chess_Container(ft.DragTarget):
    def __init__(self,board,i):
        super().__init__(
            group="chess",
            content=ft.ElevatedButton(
                text=board.chesses[i].value,
                bgcolor=ft.colors.WHITE,
                width=chess_width,height=chess_height),
            on_accept=self.drug_accept,
            # on_will_accept=self.drug_hover,
            )
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
        board.put(current_piece,self.row,self.col) 
        
        self._update()
        update_block()
        # self.show_block_color()
    def _update(self):
        self.content.text=self.chess.value
        self.content.bgcolor= self.chess.color 
        self.update()
        pass 
         
        

class Block_Container(ft.Container):
    def __init__(self, board, chess_container, ID):
        chess_container_list=[chess_container[c] for c in chess_index_in_block[ID]]
        super().__init__(
            content=ft.Row(
            width=(chess_width+spacing)*4,
            height=(chess_height+spacing*2)*3,
            controls= chess_container_list,
            wrap=True,
            run_spacing=spacing,
            # alignment="center",
            ),
            width=chess_width*3+spacing*5,
            height=chess_width*3+spacing*3,
            # alignment=ft.alignment.CENTER, 
            )
        self.ID=ID
        self.board=board 
        self.row=ID//3
        self.col=ID%3
        self.block=board.block[self.row][self.col]
        self.chess_container_list=chess_container_list
        self.border = ft.border.all(2, ft.colors.BLACK)
        # self.bgcolor=board.block[self.row][self.col].Color
        # self.bgcolor="Green" 
        # self._update()
    def _update(self):
        # self.bgcolor=self.block.color
        self.border = ft.border.all(2, self.block.color)
        print(self.block.color)
        self.update()
        pass

def click_button(e,color):
    value=int(input_text.value) % 9
    number_card.content.text=str(value)
    number_card.content.bgcolor=color
    number_card.update()
    current_piece.value=value
    current_piece.color=color

def red_button_click(e):
    return click_button(e,"Red")

def blue_button_click(e):
    return click_button(e,"Blue")



input_text=ft.TextField(width=chess_width,height=chess_height,
                    text_align="center",
                    )
red_button=ft.ElevatedButton(
            width=chess_width,
            height=chess_height,
            text="Red",icon="add",bgcolor=ft.colors.RED,
            on_click=red_button_click,
            )
blue_button=ft.ElevatedButton(
            width=chess_width,
            height=chess_height,
            text="Blue",icon="add",bgcolor=ft.colors.BLUE,
            on_click=blue_button_click)



number_card=ft.Draggable(
            group="chess",
            content=ft.ElevatedButton(
            width=chess_width,
            height=chess_height,
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
   


block_container=[Block_Container(board, chess_container,i) for i in range(9)]
global board_container
board_container=ft.Row(
        width=block_container[0].width*4 ,
        # controls=chess_container,
        controls=block_container,
        wrap=True,
        run_spacing=spacing*1,
        alignment="center",
        )

def update_block():
    for block in block_container:
        print(block.ID)
        block._update()

def main(page: ft.Page):
    # page.width=800
    page.horizontal_alignment="center"
    def drag_accept(e):
        print("OK")
        page.update()

    page.add(
        ft.Row(
            controls=[input_text,red_button,blue_button],
            alignment="center"),
        number_card,
        board_container)
        # ft.Row(
        # controls=[board_container,input_group]))
    

ft.app(target=main,view=ft.WEB_BROWSER)