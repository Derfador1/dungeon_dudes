#! /usr/bin/python3

import random
import time
import dungeon as d

random.seed(time.time())

location_num = 10

def main():
	print('Welcome to Dungeon Dudes\n')
	
	#start
	
	hero_name = ['Ash', 'Naruto', 'Ichigo', 'One Punch Man', 'Scooby Doo']
	name = random.randint(0,4)
	
	hero1 = d.Hero(hero_name[name], 10, 10)
	print(hero1)
	
	num = 0
	

	while num < location_num:
		#numb_mon = random.randint(1,3)
		room = d.Location()
		monster = d.Monster(random.randint(1,3))
		
		print(monster)
		print(room)
		
		m_initiative = monster.initiative()
		h_initiative = hero1.initiative()
		
		print('Monster:', m_initiative)
		print('Hero:', h_initiative)
		
		
		if m_initiative >= h_initiative:
			print('Monster wins initiative, it attacks')
			#monster rolls attack
			hero1.defend()

		while True:
			if hero1.char_death() == 'Dead':
				print('Your Hero has died')
				exit(1)
				#goto start
				#break
			
			menu = {'1':'List items in loot bag', '2':'Attack monster',
					'3':'Move to next location', 
					'4':'List remaining health',
					'5':'List health for monster', '6':'Quit'}
			
			options = list(menu.keys())
			options.sort()
			for entry in options:
				print(entry, menu[entry])

			selection = input("Choose an option: ")
			
			if selection == '1':
				print('1')
			elif selection == '2':
				hero1.attack(monster)
				if monster.char_death() == 'Dead':
					print('You have killed the monster, move to next location')
			elif selection == '3':
				if monster.char_death() == 'Dead':
					num += 1
					break
				else:
					print('You are still fighting')
			elif selection == '4':
				print(hero1._health)
			elif selection == '5':
				print(monster._health)
			elif selection == '6':
				print('Quitting...')
				exit(1)
			else:
				print('Unknown option selected')		
	
if __name__ == "__main__":
	main()

