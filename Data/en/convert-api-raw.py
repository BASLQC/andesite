#!/usr/bin/python3
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

def main():
	# open the api_start2.json file
	with open("api_start2.json", "r") as f:
		json_data = json.load(f)

	# loop through and rewrite ship info
	ships = json_data['api_data']['api_mst_ship']
	new_ships = []
	for ship in ships:
		# renaming keys: based on: https://kancolletool.github.io/docs/api/
		mvk(ship, 'api_sortno', 'id') # use card number as primary ID 
		mvk(ship, 'api_id', 'api_id')           # use API number as alternate ID
		mvk(ship, 'api_name', 'name')
		mvk(ship, 'api_yomi', 'kana')
		ship['name_eng'] = romkan.to_roma(ship['kana'])

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

		mvk(ship, 'api_leng', 'range')
		mvk(ship, 'api_slot_num', 'equip_slots')
		mvk(ship, 'api_buildtime', 'build_time')

		mvk(ship, 'api_broken', 'scrap_value')
		mvk(ship, 'api_powup', 'feed_value') # stat power ups when fed for modernization
		mvk(ship, 'api_backs', 'rarity')

		mvk(ship, 'api_getmes', 'get_message')

		mvk(ship, 'api_afterfuel', 'remodel_fuel_cost')
		mvk(ship, 'api_afterbull', 'remodel_ammo_cost')
		mvk(ship, 'api_fuel_max', 'max_fuel')
		mvk(ship, 'api_bull_max', 'max_ammo')
		mvk(ship, 'api_voicef', 'extra_voice_clips')

		# carrier data
		mvk(ship, 'api_maxeq', 'plane_capacity')
		
		# add to new JSON array
		new_ships.append(ship)

	print(json.dumps(new_ships, indent=2, ensure_ascii=False))

if __name__ == "__main__":
	main()
