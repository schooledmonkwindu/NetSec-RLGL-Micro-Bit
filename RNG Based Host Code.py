def on_button_pressed_a():
    global Start, Active
    Start = 1
    Active = 1
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Start
    Start = 0
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

Active = 0
Start = 0
Game_State = 0
Red_Light = 1
Green_Light = 2
Time = 0
Start = 0
Roll = 0
Active = 0
radio.set_group(1)

def on_forever():
    global Game_State, Start
    if Game_State == 1:
        basic.pause(Time * 1000)
        Game_State = 2
        basic.show_icon(IconNames.YES)
        radio.send_number(Game_State)
        Start = 1
    if Game_State == 2:
        basic.pause(Time * 1000)
        Game_State = 1
        basic.show_icon(IconNames.NO)
        radio.send_number(Game_State)
        Start = 1
basic.forever(on_forever)

def on_forever2():
    global Time, Start
    while Start == 1:
        Time = randint(1.5, 6)
        Start = 0
basic.forever(on_forever2)

def on_forever3():
    global Game_State, Active
    while Active == 1:
        Game_State = randint(1, 2)
        Active = 0
basic.forever(on_forever3)
