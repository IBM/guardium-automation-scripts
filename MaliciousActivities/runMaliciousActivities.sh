COUNTER=0
while [  $COUNTER -lt 5 ]; do
	echo The counter is $COUNTER
	let COUNTER=COUNTER+1
	# echo "Running SQL Injections (MySQL)..."
	python Injections/create_user.py testuser Guardium@1
	python Injections/sql_injection_script.py build
	python Injections/sql_injection_script.py test

	# PenTest
	echo "Running PenTest (MySQL)..."
	sleep 30
	python FailedLogin/failed_login_n_users.py
	sleep 30
	python FailedLogin/failed_login_n_attempts.py user1 3
	sleep 30
	python FailedLogin/failed_login_n_attempts.py user2 2
	sleep 30
	python FailedLogin/failed_login_n_attempts.py user3 2

	# # Threat
	echo "Running Threat..."
	python Injections/sql_injection_script.py createSales newuser
	python Injections/sql_injection_script.py createSalary newuser
	python Injections/sql_injection_script.py createAcctGroup newuser
	python Injections/sql_injection_script.py changeSales newuser
	python Injections/sql_injection_script.py changeSalary newuser
	python Injections/sql_injection_script.py callSalary rogueuser
	python Injections/sql_injection_script.py callSales rogueuser
	python Injections/sql_injection_script.py callAcctgroup rogueuser
	python Injections/sql_injection_script.py badAcctAction normaluser
	python Injections/sql_injection_script.py alterSales normaluser
	python Injections/sql_injection_script.py badSalaryAction normaluser
	python Injections/sql_injection_script.py callSalary rogueuser 
	python Injections/sql_injection_script.py callSales rogueuser
	python Injections/sql_injection_script.py callAcctgroup rogueuser


	echo "Running High Volume Activity..."
	python Threat/loopThreat.py


	INTERNAL_COUNTER=0
	while [  $INTERNAL_COUNTER -lt 2 ]; do
		echo The counter is $COUNTER
		let INTERNAL_COUNTER=INTERNAL_COUNTER+1
		python Injections/sql_injection_script.py createSalary newuser
		python Injections/sql_injection_script.py createSales newuser
		python Injections/sql_injection_script.py badSalaryAction normaluser
		python Injections/sql_injection_script.py alterSales normaluser
		python Injections/sql_injection_script.py callSalary rogueuser
		python Injections/sql_injection_script.py callSales rougeuser
		python Injections/sql_injection_script.py cleanup riskuser
	done
done
