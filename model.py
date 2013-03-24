import sqlite3

def connect_db():
	return sqlite3.connect("lottery.db")

def new_user(db, email, password, user_name):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
	result = c.execute(query, (email, password, user_name))
	db.commit()
	return result.lastrowid

def authenticate(db, email, password):
	c = db.cursor()
	query = """SELECT * from Users WHERE email=? AND password=?"""
	c.execute(query, (email, password))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "username"]
		return dict(zip(fields, result))

	return None

def get_user(db, user_id):
	c = db.cursor()
	user_id = str(user_id)
	query = """SELECT * FROM Users WHERE id=?"""
	c.execute(query, (user_id))
	row = c.fetchone()
	if row:
		fields = ["id", "email", "password", "user_name"]
		return dict(zip(fields, row))

	return None

def new_participant(db, participant_name, number_entries):
	c = db.cursor()
	query = """INSERT into Participants VALUES (NULL, ?, ?)"""
	result = c.execute(query, (participant_name, number_entries))
	db.commit()
	return result.lastrowid


def new_game(db, game):
	c = db.cursor()
	query = """INSERT into Games VALUES (NULL, ?)"""
	result = c.execute(query, (game, ))
	db.commit()
	return result.lastrowid

# get a list of all participants
def get_participants(db):
	c = db.cursor()
	query = """SELECT * from Participants"""
	c.execute(query)

	rows = c.fetchall()
	if rows:
		fields = ["participant_name", "number_entries"]
		values = []
		for row in rows:
			value = dict(zip(fields, row[1:]))
			values.append(value)
		return values
	return None

# get a list of all games
def get_games(db):
	c = db.cursor()
	query = """SELECT * from Games"""
	c.execute(query)

	rows = c.fetchall()
	if rows:
		field = ["game"]
		value = []
		for row in rows:
			values = dict(zip(field, row[1:]))
			value.append(values)
		return value
	return None

def assign_game(db, game, assigned_to):
	c = db.cursor()
	query = """UPDATE Games SET assigned_to=? WHERE game=?"""
	result = c.execute(query, assigned_to, game)
	db.commit()
	return







