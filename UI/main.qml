import QtQuick 2.3
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.1
import "util.js" as UTIL

ApplicationWindow {
    title: qsTr("TicTacToe")
    id:main
    width:800
    height:600
    visible: true
    property string position: "先手"
    property string difficult: "简单"
    property string status: "Ready"

    menuBar:MenuBar{
        Menu{
            title: "&Game"
            MenuItem{
                text:"&New Game"
                onTriggered:UTIL.createDialog()
            }
            MenuItem{
                text:"&Quit"
                onTriggered: Qt.quit()
            }
        }
        Menu{
            title: "&TreeView"
            MenuItem{
                text:"&Show"
            }
        }
    }

    statusBar: StatusBar{
        RowLayout{
            anchors.fill: parent
            Label{
                text: "Status:" + main.status + "    Difficult:" + main.difficult+ "    Position:" + main.position
            }
        }
    }

    Tictactoe{
        id:tictactoe
        anchors.centerIn: parent
    }
}

