CREATE TABLE cellphones_data (
	cellphone_id INT NOT NULL,
	brand CHAR(50) NOT NULL,
	model CHAR(50) NOT NULL,
	operating_system CHAR(50),
	PRIMARY KEY(cellphone_id)
);

CREATE TABLE cellphones_users (
	user_id INT NOT NULL,
	age INT,
	gender CHAR(50),
	PRIMARY KEY(user_id)
);

CREATE TABLE cellphones_rating (
	user_id INT NOT NULL,
	cellphone_id INT NOT NULL,
	rating INT NOT NULL,
	FOREIGN KEY(user_id) REFERENCES cellphones_users(user_id),
	FOREIGN KEY(cellphone_id) REFERENCES cellphones_data(cellphone_id)
);


