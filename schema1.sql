create table Users (
	id INTEGER PRIMARY KEY,
	email VARCHAR(64),
	password VARCHAR(64),
	user_name VARCHAR(64)
);
create table Participants (
	id INTEGER PRIMARY KEY,
	participant_name VARCHAR(255),
	number_entries INTEGER
);
create table Games (
	id INTEGER PRIMARY KEY,
	game VARCHAR(255)
);


