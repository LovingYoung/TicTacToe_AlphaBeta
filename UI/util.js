var difficult = 3
var position = 1

function createDialog() {
var dialogComponent = Qt.createComponent("MyDialog.qml");
    if(dialogComponent != Component.Ready){
        console.log(dialogComponent.errorString());
    }
    dialogComponent.createObject(main);
}

function settings(m_position,m_difficult){
    position = m_position
    difficult = m_difficult
    if(position == 1){
        main.position = "先手"
    } else {
        main.position = "后手"
    }

    if(difficult == 3){
        main.difficult = "简单"
    } else if (difficult == 5){
        main.difficult = "中等"
    } else {
        main.difficult = "困难"
    }

    main.status = "In the Game"
    initial()
}

function initial(){
    for(var i = 1; i <= 9; i++){
        tictactoe.changeState(i, "")
    }
}

function gameClick(){
    if(playerIsX()){
        piece.state = "X"
    } else{
        piece.state = "O"
    }
    //TODO

}

function playerIsX(){
    if (main.position == "先手"){
        return true
    } else{
        return false
    }
}
