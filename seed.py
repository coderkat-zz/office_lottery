import model

db = model.connect_db()
user_id = model.new_user(db, "kat@coderkat.com", "password", "kat")
participant_1 = model.new_participant(db, "Graham", 2)
