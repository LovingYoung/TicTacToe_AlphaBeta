import QtQuick 2.0
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.1
import "util.js" as UTIL


Dialog{
    id:settings
    visible: true
    title: "设置"
    property int position: 1 // 1: offensive position, 2: defensive position
    property int difficult: 3 // 3:easy, 5: medium, 7: hard

    contentItem: Rectangle {
        implicitHeight:150
        implicitWidth: 300

        Rectangle{
            width:parent.width * 0.5
            height:parent.height * 0.8
            anchors.left: parent.left

            ColumnLayout{
                anchors.fill: parent
                spacing: 10
                ExclusiveGroup{
                    id: firstOrLast
                }

                RadioButton {
                    Layout.alignment: Qt.AlignHCenter
                    id: firstButton
                    checked: true
                    text: qsTr("先手")
                    exclusiveGroup: firstOrLast
                    onClicked:{
                        settings.position = 1
                    }
                }

                RadioButton {
                    Layout.alignment: Qt.AlignHCenter
                    id: lastButton
                    text: qsTr("后手")
                    exclusiveGroup: firstOrLast
                    onClicked: {
                        settings.position = 2
                    }
                }
            }
        }

        Rectangle{
            width:parent.width * 0.5
            height:parent.height * 0.8
            anchors.right: parent.right
            ColumnLayout{
                anchors.fill: parent
                spacing: 10
                ExclusiveGroup{
                    id:difficulty
                }

                RadioButton {
                    Layout.alignment: Qt.AlignHCenter
                    id: easyButton
                    checked: true
                    text: qsTr("简单")
                    exclusiveGroup: difficulty
                    onClicked:{
                        settings.difficult = 3
                    }
                }

                RadioButton {
                    Layout.alignment: Qt.AlignHCenter
                    id: mediumButton
                    text: qsTr("中等")
                    exclusiveGroup: difficulty
                    onClicked:{
                        settings.difficult = 5
                    }
                }

                RadioButton {
                    Layout.alignment: Qt.AlignHCenter
                    id: hardButton
                    text: qsTr("困难")
                    exclusiveGroup: difficulty
                    onClicked:{
                        settings.difficult = 7
                    }
                }
            }
        }

        Rectangle{
            width:parent.width
            height: parent.height * 0.2
            anchors.bottom: parent.bottom

            Button {
                anchors.fill: parent
                id: button1
                text: qsTr("确定")
                onClicked:{
                    UTIL.settings(settings.position, settings.difficult)
                    settings.destroy()
                }
            }

        }
    }
}
