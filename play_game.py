#! /usr/bin/python3

import random
import time
import dungeon as d

random.seed(time.time())

location_num = 10

def find_max_m(monster):
	dict_m = monster.roll_atk()
	set_m = set(dict_m.values())
	max_m = max(set_m)
	print('Monster rolls:', max_m)
	return max_m
	
def find_max_h(hero1):
	dict_h = hero1.roll_atk()
	set_h = set(dict_h.values())
	max_h = max(set_h)
	print('Hero rolls:', max_h)
	return max_h
	
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
		
		print(room)
		
		m_initiative = monster.initiative()
		h_initiative = hero1.initiative()
		
		print(monster)

		if m_initiative >= h_initiative:
			print('\nMonster wins initiative, it attacks')
			max_m = find_max_m(monster)
			max_h = find_max_h(hero1)
			
			if max_m > max_h:
				print('Hero looses roll')
				monster.attack(hero1)
			else:
				print('Hero wins roll')
		else:
			print('Hero wins initiative')
			
		while True:
			print()
			
			if hero1.char_death() == 'Dead':
				print('\nYour Hero has died\n')
				exit(1)
				#goto start
							
			menu = {'1':'List items in loot bag', '2':'Attack monster',
					'3':'Move to next location', 
					'4':'List remaining health',
					'5':'List health for monster', '6':'Quit'}
			
			options = list(menu.keys())
			options.sort()
			for entry in options:
				print(entry, menu[entry])

			selection = input("\nChoose an option: ")
			
			if selection == '1':
				print('1')
			elif selection == '2':
				if monster.char_death() == 'Dead':
					print('\nYou have killed the monster, move to next location')
				else:
					max_m = find_max_m(monster)
					max_h = find_max_h(hero1)
					
					if max_h >= max_m:
						print('Monster looses roll')
						hero1.attack(monster)
					else:
						print('Monster wins roll')
					
					if monster.char_death() != 'Dead':
						print('\nMonster attacks back\n')
						max_m = find_max_m(monster)
						max_h = find_max_h(hero1)
						
						if max_m > max_h:
							print('Hero looses roll')
							monster.attack(hero1)
						else:
							print('Hero wins roll')
					else:
						print('You just killed the monster')
			elif selection == '3':
				if monster.char_death() == 'Dead':
					num += 1
					break
				else:
					print('You still need fight the monster before you!')
			elif selection == '4':
				print('\nRemaining hero health:', hero1._health)
			elif selection == '5':
				print('\nRemaining monster health:', monster._health)
			elif selection == '6':
				print('Quitting...')
				exit(1)
			else:
				print('Unknown option selected')		
	
if __name__ == "__main__":
	main()

