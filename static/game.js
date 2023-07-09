let score = 0;
let highestScore = 0;
let timesPlayed = 0

$('.form_id').on('submit',showWord, gameBoard)
 $('input').focus()
async function gameBoard(e) {
    e.preventDefault();
    console.log(this)
    let word = $('input').val()
    console.log(word)
    if(!word) return;

    $('input').val("").focus()
    console.log($('#results'))
    const res = await axios.get('/check-word', { params: {word : word}})
    console.log(res)
    let response = res.data.result;
    console.log(response)

    showWord(response,word)
    showMsg(response,word)
}

function showMsg(response, word){
    if(response === "not-on-board"){
        console.log('NOOOOOO')
        $('response').html('That word doesnt exist')
        $('#results').append('<li> That word doesnt exist on the board</li>')
    }
    if(response === "not-word"){
        $('#results').append('<li> Thats not a word, try again</li>')
    }
}
function showWord(response, word){
    if(response === 'ok'){
        score += word.length;
        $('#results').append(`<li> ${word} </li>`)
        highestScore = $(score)
        console.log(score)

    }
}

let count = 30;
let timerCountDown = setInterval(timer, 1000)

function timer() {
    count= count -1;
    endTimer();
    document.getElementById('timer').innerHTML = count + ' sec(s)'
}

function endTimer() {
    if(count < 1){
        clearInterval(timerCountDown);
        $('input').hide();
      //  $('#results').hide();
        $('timer').hide();
        $('.form_id').hide();
        $('#currentScore').append(`Game Over! Your score is: ${score} pts`);
        highestScore = document.getElementById('highestScore');
        timesPlayed += 1;
        if(score > highestScore){
            highestScore = score;
            console.log(score)
        } else{
            highestScore;
        }
        endGame();
        return;
    }
}

async function endGame(){
    res = await axios.post('/end-game', {score : score})
    console.log(res.data)
}