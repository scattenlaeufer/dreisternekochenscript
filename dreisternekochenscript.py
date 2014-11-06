#!/usr/bin/python

import os, json, argparse

parser = argparse.ArgumentParser(description='Ein Script um die Einkaufskosten für gemeinsames Kochen gerecht aufzuteilen')

parser.add_argument('-l',help='Einmal alle Daten ausgeben',action='store_true',default=False)

user_group = parser.add_argument_group('Usermanagement','was so alles zum Usermanagement nötig ist')
add_user_group = user_group.add_mutually_exclusive_group()
add_user_group.add_argument('-u','--user',metavar='ID',help='einen User managen',type=int,default=None)
add_user_group.add_argument('--add-user',metavar='NAME',type=str,help='einen neuen User hinzufügen')
user_group.add_argument('--add-money',metavar='VALUE',type=float,default=0,help='Einzahlung eines Users')

args = parser.parse_args()

print(args)

def print_number(value):
	if value < 0:
		return '\033[91m' + str(value) + '\033[0m'
	else:
		return '\033[92m' + str(value) + '\033[0m'

def list_user():
	out =  '\n ID | '+'Name'.ljust(data['meta']['max_name_length'])+' | Guthaben (€)\n'
	out += '----+'+''.ljust(data['meta']['max_name_length']+2,'-')+'+--------------\n'
	for u in sorted(data['user'].keys()):
		out += str(u).rjust(3)+' | '+data['user'][u]['name'].ljust(data['meta']['max_name_length'])+' | '+print_number(round(data['user'][u]['value'],2)).rjust(21)+'\n'
	print(out)


if os.path.isfile('dreisternekochendaten'):
	pass
else:
	data = {}
	data['user'] = {1:{'name':'Marco','value':-15.56},2:{'name':'Adrian','value':24.431},0:{'name':'Björn','value':123.34532}}
	data['events'] = []
	data['meta'] = {'max_name_length':6}

if args.l:
	list_user()
	exit()

elif args.user:
	if user in data['user']:
		pass
	elif args.add_money:
		pass

elif args.add_user:
	if len(data['user']) >= 1:
		user_id = max(data['user'].keys()) + 1
		print(user_id)
	else:
		user_id = 0
	data['user'][user_id] = {'name':args.add_user, 'value':args.add_money}

else:
	parser.print_help()

print(data)
