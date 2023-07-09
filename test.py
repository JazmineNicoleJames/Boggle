from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_generate_board(self):
        """ Test homepage generates game board, highscore and times played both equal 0 at start. """
        with self.client:
            res = self.client.get('/')
            self.assertIn('board_game', session)
            self.assertIsNone(session.get('highScore'))
            self.assertIsNone(session.get('timesPlayed'))
            self.assertIsNone(session.get('score'))

    def test_check_word(self):
        """ Test valid word returns 200 response code. """
        with self.client as client:
            with client.session_transaction() as session:
                session['board_game'] = [['B','E','A','C','H'],
                                    ['B','E','A','C','H'],
                                    ['B','E','A','C','H'],
                                    ['B','E','A','C','H'],
                                    ['B','E','A','C','H']]

            response = self.client.get('/check-word?word=beach')                
            self.assertEqual(response.json['result'], 'ok')
            self.assertEqual(response.status_code, 200)
""" 
    def test_end_game(self):
        Test if highestScore is posted on end-game.
        with self.client:
            res = self.client.post('/end-game', session)
            self.assertIn(session.post('highestScore'))
            self.asserGreater(highestScore, score) """
        

