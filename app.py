from boggle import Boggle
from flask import Flask, render_template, session, request, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
boggle_game = Boggle()
print(boggle_game.words)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'
app.debug = True
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False

game_session = 'board'

@app.route('/')
def home_page():
    """ Generate a gameboard """
    board_game = boggle_game.make_board()
    print(board_game)
    session['board_game'] = board_game
    highScore = session.get('highScore', 0)
    timesPlayed = session.get('timesPlayed', 0)
    print(session['board_game'])
    return render_template('board.html', board_game=board_game, highScore=highScore, timesPlayed = timesPlayed)


@app.route('/check-word', methods=['GET'])
def check_word():
    """Check if word is valid"""  
    word = request.args['word']
    print(word)
    board = session['board_game']
    session['board_game'] = board
    response = boggle_game.check_valid_word(board, word)
    print(response)
    return jsonify({'result': response})


@app.route('/end-game', methods=['POST'])
def end_game():
    """"Add score, highscore, and times played to session"""
    score = request.json['score']
    json['score'] = score
    high_score= session.get('highestScore', 0)
    times_played = session.get('timesPlayed', 0)
    session['timesPlayed'] = times_played + 1
    session['highestScore'] = max(score, high_score) 
    return "End of Game"