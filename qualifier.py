import challonge
import xlwt
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)

config = {}
with open("qualifier.cfg") as config_file:
    for line in config_file:
        key, val = line.partition("=")[::2]
        config[key.strip()] = val.strip()

challonge.set_credentials("Savestate", config["challonge_api_key"])

########################################

brackets = [

]

# Spille Noen
for x in range(104, 163+1):
    bracket_id = "nordicmeleenetplay-SN" + str(x)
    brackets.append(bracket_id)

# NL Netplay Weekly
for x in range(87, 153+1):
    bracket_id = "nlnetplay" + str(x)
    brackets.append(bracket_id)

# Long Live Netplay UK Weekly
#for x in range(113, 124+1):
for x in range(113, 178+1):
    bracket_id = "LLN" + str(x)
    brackets.append(bracket_id)

bracket_list = [
    # SU Smash Tournaments
    "susmash-ubocfu01",
    "susmash-sthlmnetplaytwo",
    "susmash-bz1c6ac6",
    "susmash-zr20nln8",
    "susmash-2jddw6et",
    "susmash-p4iyt7jc",
    "susmash-1yp52v99",
    "susmash-1g3bxew",
    "susmash-s64c0fwg",
    "susmash-tyly6n61",
    "susmash-5gtnam55",
    "susmash-mtor0ko1",
    "susmash-t6e9srzh",
    "susmash-4rpzds0m",
    "susmash-wzafmfng",
    "susmash-l24ae2d6",
    "susmash-rlye0tyz",
    "susmash-26ee3eh4",
    "susmash-gye1vkwq",
    "susmash-lfygseml",
    "susmash-2wo094y5",
    "susmash-svosyaw5",
    "susmash-53qxmfam",
    "susmash-n6cd3zoc",
    "susmash-v4smwcab",
    "susmash-is43i9cn",
    "susmash-4e2yi8tj",
    "susmash-6qvd3qjo",
    # EU League
    "euleague1",
    "euleague2",
    "euleague3",
    "91ihxk2b",
    "avcbl4cp",
    # Keanu Reads
    "yek94it0",
    # VFGC Weekly
    "VFGCSSBM2",
    "VFGCNETPLAY3",
    "VFGCNETPLAY4",
    "VFGCNETPLAY5",
    "VFGCNETPLAY6",
    "VFGCMELEE7",
    "VFGCMELEE8",
    "VFGCmelee9",
    "VFGCMELEETEN",
    "xt84mr93",
    "TTTbecoming16",
    "Vfgcmelee13",
    "vfgcmelee14",
    "vfgcmelee15",
    "Vfgcmelee16",
    "VFGCMelee17",
    "Vfgcmelee18",
    "Vfgcmelee19",
    "Vfgcmelee20",
    "Vfgcmelee21",
    "Vfgcmelee22",
    "Vfgcmelee23",
    "Vfgcmelee24",
    "Vfgcmelee25",
    "Vfgcmelee26",
    "Vfgcmelee27",
    "VFGCmelee28",
    "VFGCmelee29",
    "VFGCMelee30",
    "VFGCMelee31",
    "lvpws454",
    "6yxfk04t",
    # Skaraborg tournaments
    "ics029r8",
    "rda9d1lv",
    "q5sg07w0",
    # Italian weeklies
    "WINT127",
    "WINT128",
]

brackets = brackets + bracket_list

# previous_pr = [
#     "Saef",
#     "Afrodad",
#     "Savestate",
#     "Legrats",
#     "BU$TA",
#     "Lambardi",
#     "Subie",
#     "Harrison",
#     "$$$$"
#     "Lautrec"
# ]

aliases = {
    "Savestate": ["savestate", "RCS|Savestate"],
    "leffen": ["leffen", "l3ff3n"],
    "pipsqueak": ["pipsqueak", "blipsqueak"],
    "meady": ["meady", "meeady"],
    "redblaze": ["redblaze", "redssbm"],
    "daydee": ["daydee", "daydee"],
    "johnnyfight": ["johnnyfight", "johnnyfight"],
    "humpe": ["humpe", "humpe"],
    "sharp": ["sharp", "SharpSSBM"],
    "poppmaister6000": ["poppmaister6000", "poppmaister6000"],
    "eekim": ["eekim", "eekim_is_you"],
    "savestate": ["savestate", "savestate"],
    "gr4pe": ["gr4pe", "gr4pe"],
    "abbearv": ["abbearv", "abbearv"],
    "calle w": ["calle w", "calle_w"],
    "random-ness": ["random-ness", "random_ness"],
    "lillbaskern": ["lillbaskern", "lillbaskern"],
    "impx": ["impx", "impx"],
    "tellman": ["tellman", "dc_tellman"],
    "jormis": ["jormis", "jormis"],
    "jerk": ["jerk", "absurd_jerk"],
    "bigm": ["bigm", "bigmblip", "User83259", ],
    "abbson": ["abbson", "abbson"],
    "lamp": ["lamp", "lampoo", "lamp_"],
    "luigo": ["luigo", "600luigo"],
    "nils": ["nils", "nilsssbm"],
    "fatnomen": ["fatnomen", "fatnomen"],
    "smushmarth": ["smushmarth", "smushmarth"],
    "peanutz996": ["peanutz996", "peanutz996"],
    "muren": ["muren", "muren"],
    "ba$$": ["ba$$", "ba2dollarsigns"],
    "k1kk0": ["k1kk0", "k1kk0m4n"],
    "rev": ["rev", "rev"],
    "ludderix": ["ludderix", "ludderix"],
    "zedy": ["zedy", "zedylawl"],
    "sprak": ["sprak", "srpak"],
    "zing": ["zing", "zing"],
    "saftblandarn": ["saftblandarn", "saftblandarn"],
    "barba": ["barba", "niño_vfgc"],
    "nisse757": ["nisse757", "nisse757"],
    "dennis": ["dennis", "bigdenni"]
}

# not_in_region = [
#     "The Baberman",
#     "Tucker",
# ]


in_region = [
    "Savestate",
    "leffen",
    "pipsqueak",
    "meady",
    "redblaze",
    "daydee",
    "johnnyfight",
    "humpe",
    "sharp",
    "poppmaister6000",
    "eekim",
    "savestate",
    "gr4pe",
    "abbearv",
    "calle w" ,
    "random-ness",
    "lillbaskern",
    "impx",
    "tellman",
    "jormis",
    "jerk",
    "bigm",
    "abbson",
    "lamp",
    "luigo",
    "nils",
    "fatnomen",
    "smushmarth",
    "peanutz996",
    "muren",
    "ba$$",
    "k1kk0",
    "rev",
    "ludderix",
    "zedy",
    "sprak",
    "zing",
    "saftblandarn",
    "barba",
    "nisse757",
    "dennis",
]

########################################

def add_to_dict(player, players, aliases):
    name = player["username"] 
    if name == None:
        name = player["name"]

    #try:
    #    qualified = (player["final_rank"] <= 8)
    #except:
    #    qualified = True # there's not an easy
                         # way to do this unfortunately
    qualified = True

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

def check_if_beaten_pr(player, player_name, previous_pr):
    for tourney in player["sets"].keys():
        for result in player["sets"][tourney]:
            if result["loser"].lower() in [x.lower() for x in previous_pr]:
                if result["winner"].lower() == player_name.lower():
                    return True
    return False

def final_calculations(players, players_keys, ws, check=None):
    style_lose   = xlwt.easyxf('font: color-index red')
    style_win    = xlwt.easyxf('font: color-index green')
    style_header = xlwt.easyxf('font: bold on, height 160')

    r = 1
    c = 1
    max_row = 1

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
            fail_all_checks = True
            ws.write(r, c, tourney, style_header)
            print(f"  {tourney}")
            for s in player["sets"][tourney]:
                if check is not None:
                    if not check(s):
                        continue
                fail_all_checks = False
                r += 1
                if key == s["winner"]:
                    print(f"    WIN vs {s['loser']}")
                    ws.write(r, c, f"WIN vs {s['loser']}", style_win)
                else:
                    print(f"    LOSE vs {s['winner']}")
                    ws.write(r, c, f"LOSE vs {s['winner']}", style_lose)
                if (r > max_row):
                    max_row = r
            if(fail_all_checks):
                ws.write(r, c, "", style_header)
                c -= 1
        c = 1
        r = max_row + 2

def generate_grid_h2h(players, player_keys, ws, check=None):
    style_lose   = xlwt.easyxf('font: bold on, color-index black; pattern: pattern solid, fore_colour rose')
    style_win    = xlwt.easyxf('font: bold on, color-index black; pattern: pattern solid, fore_colour light_green ')
    style_header = xlwt.easyxf('font: bold on, height 160')

    print(f"!- !!!!!! GENERATING h2h GRID !!!!!! -!")

    # reference by player_key
    player_stats = {}

    # populate qualified players with empty dicts
    # fill them with all other players to make a grid
    for primary_player in players_keys:
        player_stats[primary_player] = {}
        for vs_player in players_keys:
            stats = {
                "wins": 0,
                "losses": 0,
            }
            player = players[primary_player]
            for tourney in player["sets"]:
                for s in player["sets"][tourney]:
                    if (s['loser'] == vs_player) or (s['winner'] == vs_player):
                        if primary_player == s["winner"]:
                            stats["wins"] += 1
                        else:
                            stats["losses"] += 1
            player_stats[primary_player][vs_player] = stats


    # print names to ws
    i = 2
    ws.write(1, 1, "Player", style_header)
    for player in players_keys:
        j = 2
        ws.write(1, i, player, style_header)
        ws.write(i, 1, player, style_header)
        for vs_player in players_keys:
            if vs_player == player:
                j += 1
                continue
            wins = player_stats[player][vs_player]["wins"]
            losses = player_stats[player][vs_player]["losses"]
            if wins > losses:
                ws.write(i, j, f"{wins}-{losses}", style_win)
            elif wins < losses:
                ws.write(i, j, f"{wins}-{losses}", style_lose)
            j += 1
        i += 1




match_cache = {}
tourney_cache = {}
participant_cache = {}

players = {}

failed_brackets = []

for bracket in brackets:

    try:
        tournament = challonge.tournaments.show(bracket)
    except:
        failed_brackets.append(bracket)
        continue

    t_id = tournament["id"]

    try:
        participants = challonge.participants.index(t_id)
    except:
        failed_brackets.append(bracket)
        continue

    print("Tournament: " + tournament["name"])

    try:
        match_cache[t_id] = challonge.matches.index(tournament["id"])
    except:
        failed_brackets.append(bracket)
        continue

    tourney_cache[t_id]     = tournament
    participant_cache[t_id] = participants

    for participant in participants:
        add_to_dict(participant, players, aliases)

# failed 

for bracket in failed_brackets:

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get("https://challonge.com/" + bracket, headers=headers)
        tournament_id = r.headers["X-Challonge-Cache-ID"].replace("tournament-", "")
    except Exception as e:
        print(e)
        print("UNABLE TO GET WEBPAGE " + bracket)
        continue

    try:
        tournament = challonge.tournaments.show(tournament_id)
    except Exception as e:
        print(e)
        print("FAILED BRACKET gettournament" + bracket)
        continue

    t_id = tournament["id"]

    try:
        participants = challonge.participants.index(t_id)
    except Exception as e:
        print(e)
        print("FAILED BRACKET getparticipants " + bracket)
        continue

    print("Tournament: " + tournament["name"])

    try:
        match_cache[t_id] = challonge.matches.index(tournament["id"])
    except Exception as e:
        print(e)
        print("FAILED BRACKET getmatches " + bracket)
        continue

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
threshold = 0
for player in players_keys:
    if not players[player]["qualified"]:
        players[player]["qualified"] = check_if_beaten_pr(players[player], player, previous_pr)
        if players[player]["qualified"]:
            print(f"{player} beat PR last season ...")
    # ---
    if len(players[player]["tournaments"]) < threshold:
        print(f"Removing {player} (< {threshold}) ...")
        players.pop(player)
    elif not players[player]["qualified"]:
        print(f"Removing {player} (unqualified) ...")
        players.pop(player)
    elif player.lower() not in [x.lower() for x in in_region]:
        print(f"Removing {player} (rejected) ...")
        players.pop(player)

players_keys = sorted(list(players.keys()), key=str.lower)

print(":: QUALIFYING PLAYERS ::")
print(", ".join(players_keys))
print(":: QUALIFYING PLAYER RESULTS ::")

wb = xlwt.Workbook()
ws_ps = wb.add_sheet("Player Stats")
ws_qo = wb.add_sheet("Qualified Only", cell_overwrite_ok=True)
ws_h2h = wb.add_sheet("H2H Grid", cell_overwrite_ok=True)

def qualified_only(s):
    if(s["winner"] not in players_keys):
        return False
    if(s["loser"] not in players_keys):
        return False 
    return True

final_calculations(players, players_keys, ws_ps)
final_calculations(players, players_keys, ws_qo, check=qualified_only)
generate_grid_h2h(players, players_keys, ws_h2h, check=qualified_only)

wb.save('player_info.xls')