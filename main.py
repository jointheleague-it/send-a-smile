def on_button_pressed_a():
    radio.send_string("SMILE")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    if receivedString == "SMILE":
        basic.show_icon(IconNames.HAPPY)
        music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
            music.PlaybackMode.IN_BACKGROUND)
    elif receivedString == "FROWN":
        basic.show_icon(IconNames.SAD)
        music._play_default_background(music.built_in_playable_melody(Melodies.WAWAWAWAA),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        basic.show_icon(IconNames.CONFUSED)
        music._play_default_background(music.built_in_playable_melody(Melodies.BLUES),
            music.PlaybackMode.IN_BACKGROUND)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("FROWN")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.SURPRISED)
radio.set_group(1)