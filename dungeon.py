import random
import time

random.seed(time.time())

class Character:
	def __init__(self, name, health): 
		self._name = name
		self._health = health
	
	def initiative(self):
		dice1 = random.randint(0,6)
		return dice1
		
	def char_death(self):
		output = 'Dead'
		if self._health == 0:
			return output
			
	def attack(self, other):
		other._health -= 1
		
class Monster(Character):
	def __init__(self, health, atk):
		monster_name = [
			'Skeleton','Vampire',
			'Werewolf','Sphinx',
			'Goblin','Mummy'
			]
			
		m_name = random.randint(0,5)
		super().__init__(monster_name[m_name], health)
		self._atk = atk
		
	def mon_roll_atk(self):
		dice_num = 1
		dict1 = {}
		while dice_num <= self._atk:
			dice = random.randint(1,6)
			dict1.update({dice_num:dice})
			dice_num += 1

		return dict1
		
	def __str__(self):
		output = 'Name: {0}; Health: {1}; Atk: {2}'.format(self._name, self._health, self._atk)
		return output
		
class Hero(Character):
	def __init__(self, name, health, bag_size):
		super().__init__(name, health)
		self._bag_size = bag_size
		self._lootbag = []
		
	def treasure_find(self, treasure):
		output = 'Your lootbag is full\n'
		if len(self._lootbag) < self._bag_size :
			self._lootbag.append(treasure)
		else:
			print(output)
			
	def hero_roll_atk(self):
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)
		dice3 = random.randint(1,6)
		dict1 = {'1':dice1, '2':dice2, '3':dice3}
		return dict1

	def __str__(self):
		output = 'Name: {0}; Health: {1};'.format(self._name, self._health)
		return output

class Location:
	def __init__(self):
		name_list = [
			'Doom','Poop',
			'Apples','Scorpions',
			'Hupla','Paradise'
			]
			
		rand_name = random.randint(0,5)
		self._r_name = name_list[rand_name]
			
	def __str__(self):
		output = '\nRoom of {0}'.format(self._r_name)
		return output
		

