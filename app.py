from flask import Flask, render_template
import time
import os
from threading import Thread
from tabulate import tabulate

# Importez ici vos fonctions et variables nécessaires

app = Flask(__name__)

@app.route('/')
def index():
    # Exécutez votre script principal ici
    users = []
    threads = []

    with open('users', 'r') as file:
        for line in file:
            uname, platform = line.strip().split(',')
            users.append([uname, platform])

        for user in users:
            name, platform = user
            instanceId = users.index(user)
            
            thread = Thread(target=downloadStream, args=(instanceId, name, platform))
            thread.start()
            threads.append(thread)

    # Renvoyez les données sous forme de tableau HTML
    return render_template('index.html', usernameList=usernameList)

if __name__ == '__main__':
    app.run(debug=True)
