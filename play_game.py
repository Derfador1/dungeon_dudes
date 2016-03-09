#! /usr/bin/python3

import random
import time
import dungeon as d

random.seed(time.time())

location_num = 10

def main():
	print('Welcome to Dungeon Dudes\n')
	
	hero_name = ['Ash', 'Naruto', 'Ichigo', 'One Punch Man']
	name = random.randint(0,3)
	
	hero1 = d.Hero(hero_name[name], 10, 10)
	print(hero1)
	
	num = 1
	
	while num < location_num:
	
		
		monster = d.Monster(random.randint(1,3))	
	
		print(monster)
		
		name_list = ['Doom', 'Poop', 'Apples']
		rand_name = random.randint(0,2)
		
		room = d.Location(name_list[rand_name])
		print(room)
		
		menu = {'1':'List items in loot bag', '2':'Attack monster', '3':'Move to next location', '4':'List remaining health', '5':'List health for monster'}
		
		options = list(menu.keys())
		options.sort()
		for entry in options:
			print(entry, menu[entry])

		selection = input("Choose an option: ")

		
		if selection == '1':
			print('1')
		elif selection == '2':
			print('2')
		elif selection == '3':
			print('3')
		elif selection == '4':
			print(hero1._health)
		elif selection == '5':
			print(monster._health)
		else:
			print('Unknown option selected')
			break
		
		num += 1
		
	
if __name__ == "__main__":
	main()

