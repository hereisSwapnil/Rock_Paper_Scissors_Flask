from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder='static')

player_score = 0
computer_score = 0

def decision(player_choice, computer_choice):
    '''
    rock = paper
    You Lose

    rock = scissor
    You Win
    
    paper = scissor
    You Lose

    paper = rock
    You Win

    scissor = paper
    You Win

    scissor = rock
    You Lose

    👊 🖐️ ✌️
    '''
    global player_score, computer_score
    if player_choice == computer_choice:
        return "Tie"

    elif player_choice == "👊" and computer_choice == "🖐️":
        player_score -= 1
        computer_score += 1
        return "You Lose"

    elif player_choice == "👊" and computer_choice == "✌️":
        player_score += 1
        computer_score -= 1
        return "You Win"

    elif player_choice == "🖐️" and computer_choice == "✌️":
        player_score -= 1
        computer_score += 1
        return "You Lose"

    elif player_choice == "🖐️" and computer_choice == "👊":
        player_score += 1
        computer_score -= 1
        return "You Win"

    elif player_choice == "✌️" and computer_choice == "🖐️":
        player_score += 1
        computer_score -= 1
        return "You Win"

    elif player_choice == "✌️" and computer_choice == "👊":
        player_score -= 1
        computer_score += 1
        return "You Lose"
    


@app.route('/')
def main():
    return render_template("home.html", player_choice = "", computer_choice = "", decision = "", computer_score = computer_score, player_score = player_score)

@app.route('/play', methods=['POST'])
def play():
    if request.method == 'POST':
        computer_choice = random.choice(["👊", "🖐️", "✌️"])
        player_choice = request.args["choice"]
        return render_template("home.html", player_choice = player_choice, computer_choice = computer_choice, decision = decision(player_choice, computer_choice), computer_score = computer_score, player_score = player_score)
    else:
        return render_template("home.html", player_choice = "", computer_choice = "", decision = "", computer_score = 0, player_score = 0)

@app.route('/reset')
def reset():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    return render_template("home.html", player_choice = "", computer_choice = "", decision = "", computer_score = computer_score, player_score = player_score)

app.run("0.0.0.0")