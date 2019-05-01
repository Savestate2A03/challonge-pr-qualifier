import challonge
import xlwt

challonge.set_credentials("Savestate", "YOUR API KEY HERE")

########################################

brackets = [
	"FellaFridays01_25Dubs",
	"FellaFridays02_01Singles",
	"FellaFridays02_08_19Singles",
	"FellaFridays02_15Singles",
	"FellaFridays02_22_19SIngles",
	"FellaFridays03_01_19Singles",
	"FellaFridays03_15_19Singles",
	"FellaFridays03_22_19Singles",
	"FellaFridays03_29_19",
	"FellaFridays04_05_19Singles",
	"FellaFridays04_12_19Singles",
	"FellaFridays04_26_19Singles"
]

aliases = {
	"Robert": ["Rob"],
	"SlipnSlide": ["Slip"],
	"Kackame": ["Peyton"],
	"Duk": ["DukDota", "Hassel"],
	"Timebones": ["RCS|Timebones"],
	"Vulfaerix": ["Vulf"],
	"Prince Ryuta": ["Ryuta"],
	"FacebookJoe": ["FBJoe"],
	"Johnny": ["LOVE", "Rotunda"]
}

not_in_region = [
	"SlipnSlide",
	"Kackame",
	"Duk",
	"Robert",
	"Timebones",
	"ZENT",
	"Roma",
	"blue53",
	"Dash",
	"Vulfaerix",
	"Regi",
	"Beeftip",
	"Prometheus",
	"Pelipper",
	"Willy P",
	"Rob Rowe",
	"Dagoth Dev",
	"Prince Ryuta"
]

########################################

def add_to_dict(player, players, aliases):
	name = player["name"]	

	qualified = (player["final_rank"] <= 8)

	for key in aliases:
		if name.lower() in [x.lower() for x in aliases[key]]:
			print(f"  Alias {name} -> {key}")
			name = key

	for key in players:
		if name.lower() == key.lower():
			name = key

	if name in players:
		print(f"  Updating {name} ...")
		players[name]["tournaments"].append(player["tournament_id"])
		players[name]["ids"].append(player["id"])
		if qualified:
			players[name]["qualified"] = True
	else:
		print(f"  Adding {name} to the list ...")
		players[name] = {
			"tournaments": [player["tournament_id"]],
			"sets": {},
			"ids": [player["id"]],
			"qualified": qualified
		}

match_cache = {}
tourney_cache = {}
participant_cache = {}

players = {}

for bracket in brackets:

	tournament = challonge.tournaments.show(bracket)
	t_id = tournament["id"]

	participants = challonge.participants.index(t_id)

	print("Tournament: " + tournament["name"])

	match_cache[t_id]       = challonge.matches.index(tournament["id"])
	tourney_cache[t_id]     = tournament
	participant_cache[t_id] = participants

	for participant in participants:
		add_to_dict(participant, players, aliases)

# list sets
for tourney_id in match_cache:
	matches = match_cache[tourney_id]
	for match in matches:
		match_details = {
			"id": match["id"],
			"winner": None,
			"loser": None
		}

		tourney = tourney_cache[tourney_id]["name"]

		for player in players:
			if tourney not in players[player]["sets"]:
				players[player]["sets"][tourney] = []
			if match["winner_id"] in players[player]["ids"]:
				match_details["winner"] = player
				if match["id"] not in [x["id"] for x in players[player]["sets"][tourney]]:
					players[player]["sets"][tourney].append(match_details)
			if match["loser_id"] in players[player]["ids"]:
				match_details["loser"] = player
				if match["id"] not in [x["id"] for x in players[player]["sets"][tourney]]:
					players[player]["sets"][tourney].append(match_details)

# remove players who don't qualify
players_keys = list(players.keys())
threshold = 3
for player in players_keys:
	if len(players[player]["tournaments"]) < threshold:
		print(f"Removing {player} (< {threshold}) ...")
		players.pop(player)
	elif not players[player]["qualified"]:
		print(f"Removing {player} (unqualified) ...")
		players.pop(player)
	elif player.lower() in [x.lower() for x in not_in_region]:
		print(f"Removing {player} (rejected) ...")
		players.pop(player)

players_keys = sorted(list(players.keys()), key=str.lower)

print(":: QUALIFYING PLAYERS ::")
print(", ".join(players_keys))
print(":: QUALIFYING PLAYER RESULTS ::")

wb = xlwt.Workbook()
ws = wb.add_sheet("Player Stats")

r = 1
c = 1
max_row = 1

style_lose   = xlwt.easyxf('font: color-index red')
style_win    = xlwt.easyxf('font: color-index green')
style_header = xlwt.easyxf('font: bold on')

for key in players_keys:
	player = players[key]
	print(f"{key}")
	ws.write(r, c, key)
	base_row = r
	for tourney in player["sets"]:
		if len(player["sets"][tourney]) == 0:
			continue
		c += 1
		r = base_row
		ws.write(r, c, tourney, style_header)
		print(f"  {tourney}")
		for s in player["sets"][tourney]:
			r += 1
			if key == s["winner"]:
				print(f"    WIN vs {s['loser']}")
				ws.write(r, c, f"WIN vs {s['loser']}", style_win)
			else:
				print(f"    LOSE vs {s['winner']}")
				ws.write(r, c, f"LOSE vs {s['winner']}", style_lose)
			if (r > max_row):
				max_row = r
	c = 1
	r = max_row + 2

wb.save('player_info.xls')