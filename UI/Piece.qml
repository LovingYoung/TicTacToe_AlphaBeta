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
        if(s != "X" && s != "O") return
        if(s == "X"){
            piece.state = "X"
        } else {
            piece.state = "O"
        }
    }

    function showStatus(){
        if (piece.state == ""){
            return 0;
        } else if (piece.state == "X"){
            return 1;
        } else if (piece.state == "O"){
            return 2;
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
            if (piece.state == "X" || piece.state == "O") return
            else{
                var arr = board.showStatus()
                var newarr = UTIL.gameClick(arr, piece.number);
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
        },
        State {
            name: "EMPTY"

            PropertyChanges {
                target: myImage
                source: "empty.png"
            }
        }
    ]

}
