# Assistant library
from flask import Flask
from flask_assistant import Assistant, ask, tell

# SQL query handling
from sqlalchemy import create_engine
import pandas as pd

import logging
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

driver = 'mysql+pymysql:'
user = ''
password = ''
ip = '35.187.178.245'
database = 'database'

connection_string = f'{driver}//{user}:{password}@{ip}/{database}'

#engine = create_engine(connection_string)

# Assisant code
app = Flask(__name__)
assist = Assistant(app, route='/')


@assist.action('greeting')
def greet_and_start():
    speech = "Hey! I'm your personal banking interface, mainly because your current one sucks. How can I help you?"
    return ask(speech)

if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode

@assist.action('amount-on-date', mapping={'date': 'sys.date'})
def ask_for_season(date):
    #exact_date = date[:9]
    #query = f'''SELECT SUM(amount)
    #           FROM finance
    #           WHERE date = {exact_date} AND type = 'Gasto (G)'
    #        '''
    #result = pd.read_sql(query, engine)
    #amount = result['SUM(amount)'][0] * -1
    speech = f'The amount you spent that day is {amount} euros'
    return ask(speech)
