#!/usr/bin/python3
# obtain ship info and equipment info from the authoritative source: a dump of the kancolle API
# transform the ugly api variables to things that actually make sense
import json
import re
import romkan

# rename a key in a dictionary (mv for keys)
def mvk(d, orig_key, new_key):
	d[new_key] = d.pop(orig_key)

# split up (base, max) stats
def sbm(d, orig_key, new_key):
	d[new_key] = {}
	d[new_key]['base'], d[new_key]['max'] = d.pop(orig_key, None)

def ship_info():
	# open the api_start2.json file
	with open("api_start2.json", "r") as f:
		json_data = json.load(f)

	# open the extra Ship.json file for evasion, LOS, and antisub, and others
	# sort by "index" (API ID, not card ID)
	with open("Ship.json", "r") as f:
		extra_ship_data = sorted(json.load(f), key=lambda k: k['index'])

	# loop through and rewrite ship info
	ships = json_data['api_data']['api_mst_ship']
	new_ships = []
	for ship in ships:
		# なし (nashi) means Null, an unused ID
		if romkan.to_roma(ship['api_name']) == "nashi":
			ships.remove(ship)
			continue
		
		# renaming keys: based on: https://kancolletool.github.io/docs/api/
		mvk(ship, 'api_sortno', 'id') # use card number as apparent ID 
		mvk(ship, 'api_id', 'api_id')           # use API number as primary ID
		mvk(ship, 'api_name', 'name')
		mvk(ship, 'api_yomi', 'kana')
		
		# don't create romanizations of ships without kana
		if ship['kana'] != "":
			ship['name_roma'] = romkan.to_roma(ship['kana'])
		else:
			ship['name_roma'] = ""

		mvk(ship, 'api_stype', 'ship_class')
		mvk(ship, 'api_afterlv', 'remodel_min_lv')
		mvk(ship, 'api_aftershipid', 'remodel_ship_id')

		# split up (base, max) stats
		sbm(ship, 'api_taik', 'hp')
		sbm(ship, 'api_souk', 'armor')
		sbm(ship, 'api_houg', 'firepower')
		sbm(ship, 'api_raig', 'torpedo')
		sbm(ship, 'api_tyku', 'antiair')
		sbm(ship, 'api_luck', 'luck')
		
		# derived variables from Ship.json
		# look through extra_ship_data for matching index, then grab data from there
		for extra_ship in extra_ship_data:
			if (extra_ship['index'] == ship['api_id']):
				# ASW: Anti-sub
				ship['antisub'] = extra_ship['antisub']
				
				# LOS: line-of-sight
				ship['line_of_sight'] = extra_ship['lineOfSight']
				
				# evasion
				ship['evasion'] = extra_ship['evasion']
				
				# illustrator
				if 'illustrator' in extra_ship.keys():
					if extra_ship['illustrator'] != 0:
						ship['illustrator'] = extra_ship['illustrator']
					else:
						ship['illustrator'] = ""
				else:
					ship['illustrator'] = ""
					
				# seiyuu: voice actor
				if 'cv' in extra_ship.keys():
					if extra_ship['cv'] != 0:
						ship['seiyuu'] = extra_ship['cv']
					else:
						ship['seiyuu'] = ""
				else:
					ship['seiyuu'] = ""
			
			else: # give default values if info not found
				ship['antisub'] = 0
				ship['line_of_sight'] = 0
				ship['evasion'] = 0
				ship['illustrator'] = ""
				ship['seiyuu'] = ""
				
		#print(ship['api_id'], ship['name_roma'], extra_ship_data[ship['api_id'] - 1])
		
		"""
		# optional variables, set to [] or 0 if nonexistent
		if 'api_tais' in ship:
			sbm(ship, 'api_tais', 'antisub')
		else:
			ship['antisub'] = [0, 0]
		
		if 'api_saku' in ship:
			sbm(ship, 'api_saku', 'line_of_sight')
		else:
			ship['line_of_sight'] = [0, 0]

		if 'api_kaih' in ship:
			sbm(ship, 'api_kaih', 'evasion')
		else:
			ship['evasion'] = [0, 0]
		"""

		mvk(ship, 'api_leng', 'range')
		mvk(ship, 'api_slot_num', 'equip_slots')
		mvk(ship, 'api_buildtime', 'build_time')

		mvk(ship, 'api_broken', 'scrap_value')
		mvk(ship, 'api_powup', 'feed_value') # stat power ups when fed for modernization
		mvk(ship, 'api_backs', 'rarity')

		mvk(ship, 'api_getmes', 'get_message')

		mvk(ship, 'api_afterfuel', 'remodel_fuel_cost') # apparently this is steel not fuel. The kancolle devs themselves may have misspelled it and neglected to fix it.
		mvk(ship, 'api_afterbull', 'remodel_ammo_cost')
		mvk(ship, 'api_fuel_max', 'max_fuel')
		mvk(ship, 'api_bull_max', 'max_ammo')
		mvk(ship, 'api_voicef', 'extra_voice_clips')

		# carrier data
		mvk(ship, 'api_maxeq', 'plane_capacity')
		
		# add to new JSON array
		new_ships.append(ship)

	return json.dumps(new_ships, indent=2, ensure_ascii=False)

def ship_types():
	# open the api_start2.json file
	with open("api_start2.json", "r") as f:
		json_data = json.load(f)

	# loop through and rewrite ship info
	types = json_data['api_data']['api_mst_stype']
	new_typess = []
#	for type in types:
#		mvk(type)

	print(types)

def equip_info():
	# open the api_start2.json file
	with open("api_start2.json", "r") as f:
		json_data = json.load(f)

	# loop through and rewrite ship info
	equips = json_data['api_data']['api_mst_ship']
	new_equip = []
#	for equip in equips:
#		mvk(equip, )

def main():
#	print(ship_types())
	print(ship_info())

if __name__ == "__main__":
	main()
