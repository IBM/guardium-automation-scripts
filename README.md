## Prerequisite and updates required

1. Script will run in python environment.
2. Create 1 user with DBA permission. and other few users as normal user. You can also user the createUser script present 
inside Injections folder for creating normal type of user. 

    Sample to call the script "python Injections/create_user.py 'username' 'password'"

3. In the script, I have created four users, newuser being user with DBA permission while rogueuser, normaluser, riskuser 
are normal type of user.

4. Update all the respective users in the script for getting different logs for different users.

5. Update the user if required in failed_login_attempts. This could be any random name for the user

6. There is config.ini file Here is the details of the params in the file.
    1. loop_range: This is for setting the range for loopThreat.py file
    2. failed_login_array: This is array of users passed to failed login users.
    3. host: Database server Host 
    4. database: Database name
    5. port: Database server port
    6. user: User with DBA permission
    7. passwd: Password for user in point 6


## Run the script with following steps

1. Add the required details in config.ini
2. cd MaliciousActivities/
3. sh runMaliciousActivities.sh
