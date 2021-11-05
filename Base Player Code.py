def on_received_number(receivedNumber):
    global Game_State
    Game_State = receivedNumber
radio.on_received_number(on_received_number)

Microbit_Movement = 0
Game_State = 0
Game_State = 0
Red_Light = 1
Green_Light = 2
Alive = 10
radio.set_group(1)

def on_forever():
    if Alive == 10:
        if Game_State == Green_Light:
            basic.show_icon(IconNames.YES)
        if Game_State == Red_Light:
            basic.show_icon(IconNames.NO)
basic.forever(on_forever)

def on_forever2():
    global Microbit_Movement, Alive
    if Game_State == Red_Light:
        Microbit_Movement = abs(input.acceleration(Dimension.STRENGTH) - 1024)
        if Microbit_Movement > 100:
            basic.show_leds("""
                . # # # .
                                # . # . #
                                # # # # #
                                . # # # .
                                . # # # .
            """)
            Alive = 11
basic.forever(on_forever2)
