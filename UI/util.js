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
    if(main.position == "后手"){
        var tempArr = new Array();
        for(var i = 0; i < 9; i++){
            tempArr[i] = 0;
        }
        gameStart(tempArr);
    }
}

function initial(){
    for(var i = 1; i <= 9; i++){
        tictactoe.changeState(i, "EMPTY");
    }
    tictactoe.setStatus([0,0,0,0,0,0,0,0,0]);
}

function gameStart(arr){
    media.status = arr;
    media.nextStep()
    var newarr = media.status
    tictactoe.setStatus(newarr);
    var isComplete = media.isComplete;
    var winner = media.winner;
    if(isComplete != 0){
        afterComplete(winner);
    }
}

function gameClick(arr, number){
    if(playerIsX()){
        piece.state = "X"
        arr[number-1] = 1;
    } else{
        piece.state = "O"
        arr[number-1] = 2;
    }
    var isComplete = media.isComplete;
    var winner = media.winner;
    if(isComplete != 0){
        afterComplete(winner);
    }
    gameStart(arr);
}

function playerIsX(){
    return true
}

function afterComplete(winner){
    if(winner == 1)
        main.status = "Game Complete, Winner is Player";
    if(winner == 2)
        main.status = "Game Complete, Winner is Computer";
    else
        main.status = "Game Complete, Draw Game";
}
