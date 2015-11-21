import QtQuick 2.0

Rectangle{
    id:board
    width:500
    height:500
    color:"transparent"
    Image{
        source: "board.png"
        anchors.fill:parent
    }

    function changeState(number, state){
        if(number == 1) piece1.changeState(state)
        if(number == 2) piece2.changeState(state)
        if(number == 3) piece3.changeState(state)
        if(number == 4) piece4.changeState(state)
        if(number == 5) piece5.changeState(state)
        if(number == 6) piece6.changeState(state)
        if(number == 7) piece7.changeState(state)
        if(number == 8) piece8.changeState(state)
        if(number == 9) piece9.changeState(state)
    }

    function showStatus(){
        var arr = new Array()
        arr[0] = piece1.showStatus()
        arr[1] = piece2.showStatus()
        arr[2] = piece3.showStatus()
        arr[3] = piece4.showStatus()
        arr[4] = piece5.showStatus()
        arr[5] = piece6.showStatus()
        arr[6] = piece7.showStatus()
        arr[7] = piece8.showStatus()
        arr[8] = piece9.showStatus()
        return arr
    }

    function setStatus(arr){
        for(var i = 0; i < 9; i++){
            if(arr[i] == 0) continue
            else if(arr[i] == 1)
                board.changeState((i+1), "X");
            else
                board.changeState((i+1), "O");
        }
    }


    Piece{
        id:piece1
        anchors.verticalCenterOffset: -151
        anchors.horizontalCenterOffset: -150
        anchors.centerIn: parent
        number: 1
    }

    Piece {
        id: piece2
        number: 2
        x: -8
        y: 3
        anchors.verticalCenterOffset: -151
        anchors.horizontalCenterOffset: 0
        anchors.centerIn: parent
    }

    Piece {
        id: piece3
        number: 3
        x: -10
        y: -6
        anchors.verticalCenterOffset: -151
        anchors.centerIn: parent
        anchors.horizontalCenterOffset: 158
    }

    Piece {
        id: piece4
        number: 4
        x: -9
        y: -9
        anchors.verticalCenterOffset: 0
        anchors.centerIn: parent
        anchors.horizontalCenterOffset: -150
    }

    Piece {
        id: piece5
        number: 5
        x: -17
        y: -6
        anchors.verticalCenterOffset: 0
        anchors.centerIn: parent
        anchors.horizontalCenterOffset: 0
    }

    Piece {
        id: piece6
        number: 6
        x: -19
        y: -15
        anchors.verticalCenterOffset: 0
        anchors.centerIn: parent
        anchors.horizontalCenterOffset: 158
    }

    Piece {
        id: piece7
        number: 7
        x: 4
        y: 4
        anchors.verticalCenterOffset: 146
        anchors.centerIn: parent
        anchors.horizontalCenterOffset: -150
    }

    Piece {
        id: piece8
        number: 8
        x: -4
        y: 7
        anchors.verticalCenterOffset: 146
        anchors.centerIn: parent
        anchors.horizontalCenterOffset: 0
    }

    Piece {
        id: piece9
        number: 9
        x: -6
        y: -2
        anchors.verticalCenterOffset: 146
        anchors.centerIn: parent
        anchors.horizontalCenterOffset: 158
    }
}
