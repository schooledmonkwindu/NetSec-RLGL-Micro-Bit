def on_button_pressed_a():
    global Game_State
    Game_State = Green_Light
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Game_State
    Game_State = Red_Light
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

Green_Light = 0
Red_Light = 0
Game_State = 0
Game_State = 0
Red_Light = 1
Green_Light = 2
radio.set_group(1)

def on_forever():
    radio.send_number(Game_State)
basic.forever(on_forever)
