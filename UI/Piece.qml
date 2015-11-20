import QtQuick 2.0
import "util.js" as UTIL

Rectangle{
    id:piece
    height:110
    width:110
    color:"transparent"
    property int number : 0
    property string status: main.status

    function changeState(s){
        if(s != "X" && s != "Y") return
        if(s == "X"){
            piece.state = "X"
        } else {
            piece.state = "Y"
        }
    }

    Image {
        id: myImage
        anchors.fill: parent
        source: "empty.png"
    }

    MouseArea{
        anchors.fill:parent
        onClicked:{
            if (main.status != "In the Game" && piece.state == "") return
            else{
                UTIL.gameClick(piece.number)
            }
        }
    }

    states: [
        State {
            name: "O"

            PropertyChanges {
                target: myImage
                source: "O.png"
            }
        },
        State {
            name: "X"

            PropertyChanges {
                target: myImage
                source: "X.png"
            }
        }
    ]

}
