#! /usr/bin/python3

import random
import time
import os
import dungeon as d

random.seed(time.time())

num_of_loc = 10

# grabs the dictionary fron mon roll atk and casts it as a set
# then finds the max of said set which is the value we want
def find_max_mdice(monster):
	dict_m = monster.mon_roll_atk()
	set_m = set(dict_m.values())
	max_m = max(set_m)
	print('Monsters highest dice roll:', max_m)
	return max_m

# grabs the dictionary fron hero roll atk and casts it as a set
# then finds the max of said set which is the value we want	
def find_max_hdice(hero1):
	dict_h = hero1.hero_roll_atk()
	set_h = set(dict_h.values())
	max_h = max(set_h)
	print('Hero highest dice roll:', max_h)
	return max_h

# simple check for if monster attacks first	
def monster_check(max_m, max_h, monster, hero1):
	if max_m >= max_h:
		print('Monster wins, Hero takes damage')
		monster.attack(hero1)
	else:
		print('Monster looses, Hero defends')

# simple check for if hero attacks first			
def hero_check(max_m, max_h, monster, hero1):
	if max_h >= max_m:
		print('Hero wins, Monster takes damage')
		hero1.attack(monster)
	else:
		print('Hero looses, Monster defends')

def menu_print(menu):
	options = list(menu.keys())
	options.sort()
	for entry in options:
		print(entry, menu[entry])

# checks to see if an atk potion is in the lootbag
def check_lootbag(hero1):
		for item in hero1._lootbag:
			if item == 'Atk Potion':
				return True
		
		return False
		
def potion_remove(hero1):
	for item in hero1._lootbag:
		if item == 'Atk Potion':
			hero1._lootbag.remove(item)
			
def lootbag_print(hero1):
	if not len(hero1._lootbag):
		print('Nothing at the moment')
		
	for item in hero1._lootbag:
		print(item)
					
def atk_func(monster, hero1, potion_true):
	max_m = find_max_mdice(monster)
	max_h = find_max_hdice(hero1)
	
	# re rolls a new dice to see if a better value could be obtained
	# only if a ption was used
	if potion_true == 1:
		new_roll = random.randint(1,6)
		if new_roll > max_h:
			max_h = new_roll
		print('Potion activated new roll:', max_h)
	
	hero_check(max_m, max_h, monster, hero1)

def treasure_check(treasure_list, treasure_numb, hero1):
	print('You just killed the last monster')
	if treasure_numb == 1:
		print('You found treasure')
		treasure = random.randint(0,5)
		# if treasure_numb is 1, this is were we create and add treasure
		hero1.treasure_find(treasure_list[treasure])
	else:
		print('There was no treasure in this room')

def main():
	os.system('clear')

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
		'Atk Potion', 'Poison Dagger',
		'Sword of Doom', 'Shield of Weakness',
		'Poop(the hell did you pick this up for!?!?!)',
		'Gold'
		]

	name = random.randint(0,4)
	
	hero1 = d.Hero(hero_name[name], 10)
	print(hero1)
	
	num = 1
	
	potion_true = 0

	while num <= num_of_loc:
		# random number chosen for monsters		
		mon_numb = random.randint(1,3)
		# random number chosen if there is treasure or not
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
			
			print()
		else:
			# optional choices for flourish of player running if initiative won
			choice = input('Hero wins initiative, Do you wish to skip this fight?(y or n)')
			if choice == 'y':
				print('Proceeding in sneak mode to next room...\n')
				num += 1
				continue
			elif choice	== 'n':
				print('Entering Menu...\n')
			else:
				print('Incorrect option...begin fighting\n')
						
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
				os.system('clear')
				
				lootbag_print(hero1)
				
				if check_lootbag(hero1):
					while True:
						select = input('Do you wish to use atk potion?(y or n): ')
						if select == 'y':
							potion_true = 1
							break
						elif select == 'n':
							potion_true = 0
							break
						else:
							print('That was not proper input')
											
				if potion_true == 1:
					# if the potion is used we remove it from the bag
					potion_remove(hero1)
			elif selection == '2':
				os.system('clear')

				if monster.char_death() == 'Dead':
						print('You have killed all the monsters, move to next location')
				else:
					atk_func(monster, hero1, potion_true)
					if monster.char_death() != 'Dead':
						print('\nMonster attacks back\n')
						max_m = find_max_mdice(monster)
						max_h = find_max_hdice(hero1)
						
						monster_check(max_m, max_h, monster, hero1)
					else:
						# check made if there was more then one monster_numb
						if mon_numb > 1:
							print('\nYou have killed the monster, however there is another monster')
							mon_numb -= 1
							# we re-call monster to new random values
							monster = d.Monster(random.randint(1,3), random.randint(1,3))
							print('Next monster ->', monster)
						else:
							treasure_check(treasure_list, treasure_numb, hero1)
								
					potion_true = 0
			elif selection == '3':
				os.system('clear')
				if mon_numb == 1:
					if monster.char_death() == 'Dead':
						num += 1
						break
					else:
						print('You still need to fight the monster before you!')
				else:
					print('There are multiple monsters left')
					
			elif selection == '4':
				os.system('clear')
				print('Remaining hero health:', hero1._health)
			elif selection == '5':
				os.system('clear')
				print('Remaining monster health:', monster._health)
			elif selection == '6':
				os.system('clear')
				print('Quitting...')
				exit(1)
			else:
				os.system('clear')
				print('Unknown option selected')
			
			print()
				
	print('You have won in this Dungeon')		
	
if __name__ == "__main__":
	main()

