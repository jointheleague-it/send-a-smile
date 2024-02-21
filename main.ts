input.onButtonPressed(Button.A, function () {
    radio.sendString("SMILE")
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "SMILE") {
        basic.showIcon(IconNames.Happy)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpUp), music.PlaybackMode.InBackground)
    } else if (receivedString == "FROWN") {
        basic.showIcon(IconNames.Sad)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Wawawawaa), music.PlaybackMode.InBackground)
    } else {
        basic.showIcon(IconNames.Confused)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Blues), music.PlaybackMode.InBackground)
    }
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("FROWN")
})
basic.showIcon(IconNames.Surprised)
radio.setGroup(1)
