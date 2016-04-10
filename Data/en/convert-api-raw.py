#!/usr/bin/python3
import json
import re

# rename a key in a dictionary (mv for keys)
def mvk(d, orig_key, new_key):
	d[new_key] = d.pop(orig_key)

# split up (base, max) stats
def sbm(d, orig_key, new_key):
	d[new_key] = {}
	d[new_key]['base'], d[new_key]['max'] = d.pop(orig_key, None)

# open the api_start2.json file
with open("api_start2.json", "r") as f:
	json_data = json.load(f)

# ship info
ship = json_data['api_data']['api_mst_ship'][0]

# renaming keys: based on: https://kancolletool.github.io/docs/api/
# orig, new
mvk(ship, 'api_id', 'id')
mvk(ship, 'api_sortno', 'card_num')
mvk(ship, 'api_name', 'name')
mvk(ship, 'api_yomi', 'kana')

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
mvk(ship, 'api_pow_up', 'feed_value') # stat power ups when fed for modernization
mvk(ship, 'api_backs', 'rarity')

mvk(ship, 'api_getmes', 'get_message')

mvk(ship, 'api_afterfuel', 'remodel_fuel_cost')
mvk(ship, 'api_afterfuel', 'remodel_ammo_cost')
mvk(ship, 'api_fuel_max', 'max_fuel')

# carrier data
mvk(ship, 'api_max_eq', 'plane_capacity')

print(json.dumps(ships, indent=2, ensure_ascii=False))

# dump the mst_ship stuff to raw data
#with open('ships_raw.json', 'w') as f:
#	f.write(json.dumps(d['data']['mst_ship'], indent=2, ensure_ascii=False)) 
