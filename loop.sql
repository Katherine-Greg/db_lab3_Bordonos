--SELECT * FROM cellphones_users;
DO 
$$
DECLARE
	us_id INT;
	us_age INT;
	us_gender CHAR(25);
BEGIN
	us_id := 150;
    FOR counter IN 1..10
        LOOP
		   INSERT INTO cellphones_users(user_id, age, gender) 
		   VALUES (us_id + counter, 20 + counter, 'male');
        END LOOP;
END;
$$


