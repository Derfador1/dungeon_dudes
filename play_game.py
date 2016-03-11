#! /usr/bin/python3

import random
import time
import dungeon as d

random.seed(time.time())

num_of_loc = 10

def find_max_mdice(monster):
	dict_m = monster.mon_roll_atk()
	set_m = set(dict_m.values())
	max_m = max(set_m)
	print('Monsters highest dice roll:', max_m)
	return max_m
	
def find_max_hdice(hero1):
	dict_h = hero1.hero_roll_atk()
	set_h = set(dict_h.values())
	max_h = max(set_h)
	print('Hero highest dice roll:', max_h)
	return max_h
	
def monster_check(max_m, max_h, monster, hero1):
	if max_m >= max_h:
		print('Monster wins, Hero takes damage\n')
		monster.attack(hero1)
	else:
		print('Monster looses, Hero defends\n')
		
def hero_check(max_m, max_h, monster, hero1):
	if max_h >= max_m:
		print('Hero wins, Monster takes damage\n')
		hero1.attack(monster)
	else:
		print('Hero looses, Monster defends\n')

def menu_print(menu):
	options = list(menu.keys())
	options.sort()
	for entry in options:
		print(entry, menu[entry])

def main():
	print('Welcome to Dungeon Dudes\n')
	
	print('You are a world renowned fighter who '
		  'has taken to searching dungeons!')
		  
	print('Many such dungeons are filled with monsters who '
		  'will gladly strip your bones of all flesh...')
		  
	print('Let us see if the dungeons bless you with '
		  'treasure or curse you with death!\n')
	
	hero_name = [
		'Ash', 'Naruto',
		'Ichigo','One Punch Man',
		'Scooby Doo'
		]
		
	treasure_list = [
		'Sword','Bow',
		'Dagger','Gold',
		'Poop(the hell did you pick this up for!?!?!)',
		'Potion'
		]

	name = random.randint(0,4)
	
	hero1 = d.Hero(hero_name[name], 10)
	print(hero1)
	
	num = 1

	while num <= num_of_loc:
		mon_numb = random.randint(1,3)
		treasure_numb = random.randint(0,1)
				
		room = d.Location()
		monster = d.Monster(random.randint(1,3), random.randint(1,3))
				
		m_initiative = monster.initiative()
		h_initiative = hero1.initiative()

		print(room)	
		print(monster)
						
		if m_initiative > h_initiative:
			print('\nMonster wins initiative, it attacks')
			max_m = find_max_mdice(monster)
			max_h = find_max_hdice(hero1)
			
			monster_check(max_m, max_h, monster, hero1)
		else:
			choice = input('Hero wins initiative, Do you wish to skip this fight?(y or n)')
			if choice == 'y':
				print('Proceeding in sneak mode to next room...')
				num += 1
				continue
			elif choice	== 'n':
				print('Entering Menu...')
			else:
				print('Incorrect option...begin fighting')
				
				
		while True:
			if hero1.char_death() == 'Dead':
				print('Your Hero made it to level', num)
				exit(1)
							
			menu = {
				'1':'List items in loot bag',
				'2':'Attack monster',
				'3':'Move to next location', 
				'4':'List remaining health',
				'5':'List health for monster',
				'6':'Quit'
				}
			
			menu_print(menu)

			selection = input("\nChoose an option: ")
			
			if selection == '1':
				for item in hero1._lootbag:
					print(item)		
			elif selection == '2':
				if monster.char_death() == 'Dead':
						print('\nYou have killed all the monsters, move to next location')
				else:
					max_m = find_max_mdice(monster)
					max_h = find_max_hdice(hero1)
					
					hero_check(max_m, max_h, monster, hero1)
					
					if monster.char_death() != 'Dead':
						print('\nMonster attacks back\n')
						max_m = find_max_mdice(monster)
						max_h = find_max_hdice(hero1)
						
						monster_check(max_m, max_h, monster, hero1)
					else:
						if mon_numb > 1:
							print('\nYou have killed the monster, however there is another monster')
							mon_numb -= 1
							monster = d.Monster(random.randint(1,3), random.randint(1,3))
							print('Next monster ->', monster)
						else:
							print('You just killed the monster')
							if treasure_numb == 1:
								print('You found treasure')
								treasure = random.randint(0,4)
								hero1.treasure_find(treasure_list[treasure])
							else:
								print('There was no treasure in this room')
			elif selection == '3':
				if mon_numb == 1:
					if monster.char_death() == 'Dead':
						num += 1
						break
					else:
						print('You still need to fight the monster before you!')
				else:
					print('There are multiple monsters left')
					
			elif selection == '4':
				print('\nRemaining hero health:', hero1._health)
			elif selection == '5':
				print('\nRemaining monster health:', monster._health)
			elif selection == '6':
				print('Quitting...')
				exit(1)
			else:
				print('Unknown option selected')
				
			print()
				
	print('You have won in this Dungeon')		
	
if __name__ == "__main__":
	main()

