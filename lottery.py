from flask import Flask, render_template, request, redirect
import model, random

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", user_name="kat")

@app.route("/the_lottery")
def the_lottery():
	db = model.connect_db()
	participants_from_db = model.get_participants(db)
	games_from_db = model.get_games(db)

	participant_list = []
	number_entry_list = []

	for participant in participants_from_db:
	 	participant_list.append(participant["participant_name"])
		number_entry_list.append(participant["number_entries"])
	
	participants = zip(participant_list, number_entry_list)

	games_list = []
	for game in games_from_db:
		games_list.append(game["game"])

	return render_template("set_up.html", participants=participants, games=games_list)

@app.route("/show_setup")
def show_setup():
	db = model.connect_db()
	participants_from_db = model.get_participants(db)
	games_from_db = model.get_games(db)

	participant_list = []
	number_entry_list = []

	for participant in participants_from_db:
	 	participant_list.append(participant["participant_name"])
		number_entry_list.append(participant["number_entries"])
	
	participants = zip(participant_list, number_entry_list)

	games_list = []
	for game in games_from_db:
		games_list.append(game["game"])

	return render_template("show_setup.html", participants=participants, games=games_list)

@app.route("/save_participant", methods=["POST"])
def save_participant():
	participant_name = request.form['participant_name']
	number_entries = request.form['number_entries']
	db = model.connect_db()
	participant_id = model.new_participant(db, participant_name, number_entries)
	return redirect("/show_setup")

@app.route("/save_game", methods=["POST"])
def save_game():
	new_game_id = request.form['game']
	db = model.connect_db()
	game_id = model.new_game(db, new_game_id)
	return redirect("/show_setup")

@app.route("/winners")
def winners():
	db = model.connect_db()
	participants_from_db = model.get_participants(db)
	games_from_db = model.get_games(db)
	print participants_from_db

	entries = []

	for item in participants_from_db:
		entry = item['number_entries']
		person = item['participant_name']
		for i in range(entry):
			entries.append(person)
	random.shuffle(entries)
	
	games_list = []
	for game in games_from_db:
		games_list.append(game["game"])
	random.shuffle(games_list)

	decisions = {}
	a = 0
	while a < len(entries):
		if entries[a] in decisions:
			decisions[entries[a]].append(games_list[a])
		else:
			decisions[entries[a]] = [games_list[a]]
		a +=1
	print decisions



	return render_template("winners.html", winners = decisions)

if __name__ == "__main__":
	app.run(debug=True)