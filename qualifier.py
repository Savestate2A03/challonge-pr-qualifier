import challonge
import xlwt
from pprint import pprint

config = {}
with open("qualifier.cfg") as config_file:
    for line in config_file:
        key, val = line.partition("=")[::2]
        config[key.strip()] = val.strip()

challonge.set_credentials("Savestate", config["challonge_api_key"])

########################################

brackets = [
    "MystiksMansion1",
    "w7rsagyh",
    "sgcnhto3",
    "1l5rrznq",
    "FellaFridays09_06_19Singles",
    "1nv7x0rc",
    "FellaFridays09_20_19Singles",
    "FellaFridays09_27_19",
    "FellaFridays10_4_19Singles",
    "FellaFridays10_18_19Singles",
    "FellaFridays10_25_19Singles",
    "FellaFridays11_1_19Singles",
    "FellaFridays118",
    "FellaFridays11_15_19Singles",
    "FellaFridays11_22_19",
    "Rite1PoolA",
    "Rite1PoolB",
    "Rite2"
    ]

previous_pr = [
    "Saef",
    "Afrodad",
    "Savestate",
    "Legrats",
    "BU$TA",
    "Lambardi",
    "Subie",
    "Harrison",
    "$$$$"
    "Lautrec"
]

aliases = {
    "Robert": ["Rob"],
    "Chi": ["chi"],
    "SlipnSlide": ["Slip", "slipnslide"],
    "Kackame": ["Peyton"],
    "Duk": ["DukDota", "Hassel"],
    "Timebones": ["RCS|Timebones"],
    "Vulfaerix": ["Vulf"],
    "Prince Ryuta": ["Ryuta"],
    "FacebookJoe": ["FBJoe", "facebookjoe", "fb joe", "FacebookJoe (3-2 vs ADMJ)"],
    "Johnny": ["LOVE", "Rotunda"],
    "Ogre": ["True Ogre"],
    "Redman": ["Locke"],
    "TwistyTreats": ["Twisty"],
    "Lambardi": ["lamb"],
    "Lautrec": ["lautrec"],
    "Saef": ["saef", "Saef*", "(put a marble on my coffin)"],
    "Subie": ["subie"],
    "IHOP | Dan": ["ihop dan"],
    "Adonis": ["adonis"],
    "BU$TA": ["busta"],
    "HiFi": ["hifi"],
    "Sky": ["sky"],
    "Act": ["act"],
    "Andy": ["andy"],
    "Angel": ["angel"],
    "Coconut Man": ["Coconut Man"],
    "EMB": ["emb"],
    "Grit": ["grit"],
    "Exposed": ["exposed"],
    "Willy P": ["willypee", "WillyP"],
    "Hennessy": ["hennessy"],
    "TheArq": ["arq", "Krillin", "krillin the villian", "Krillin the Villain", "KrillintheVillian"],
    "MountainDrew": ["mountaindrew"],
    "Music": ["music"],
    "Obscurity": ["obscurity"],
    "Orcus": ["orcus"],
    "Choi": ["choi"],
    "Osmics": ["osmics"],
    "Paradigm": ["paradigm"],
    "Siddward": ["siddward"],
    "YV": ["yv"],
    "GCS": ["gcs"],
    "Harrison": ["kid fantastic", "plug named david :)"],
    "Afrodad": ["afrodad"],
    "Pelipper": ["pelipper"],
    "Shenal": ["$henal"],
    "Subie": ["$ubie"],
    "Dev": ["Dagoth Dev"],
    "Hollow": ["hollow"],
    "Legrats": ["legrats"],
    "Magnus": ["Magnus*"],
    "Mystik": ["mystik", "mystic"],
    "One Approved": ["one approved", "oneapproved"],
    "PapaSquat": ["poppasquat"],
    "Sarge": ["sarge"],
    "Savestate": ["savestate", "RCS|Savestate"],
    "Shenal": ["shenal", "shenal*"],
    "Subie": ["subie"]
}

not_in_region = [
    "The Baberman",
    "Tucker",
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
    "Prince Ryuta",
    "Ender",
    "Charlie Nash",
    "Sulla",
    "Chi",
    "GCS",
    "IHOP | Dan",
    "jwilli",
    "MEAT",
    "Tiger",
    "TwistyTreats",
    "Adonis",
    "Babich",
    "HiFi",
    "Jonathan Cotto",
    "Grit",
    "Andy",
    "Coconut Man",
    "Exposed",
    "Willy P",
    "Hennessy", 
    "muffinman",
    "Obscurity",
    "MountainDrew",
    "Osmics",
    "Paradigm",
    "YV",
    "Lambardi",
    "Bongo Beat",
    "Corolla",
    "Dev"
]

########################################

def add_to_dict(player, players, aliases):
    name = player["name"]   

    try:
        qualified = (player["final_rank"] <= 8)
    except:
        qualified = True # there's not an easy
                         # way to do this unfortunately

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
                ws
                ws.write(r, c, "", style_header)
                c -= 1
        c = 1
        r = max_row + 2


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
threshold = 2
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
    elif player.lower() in [x.lower() for x in not_in_region]:
        print(f"Removing {player} (rejected) ...")
        players.pop(player)

players_keys = sorted(list(players.keys()), key=str.lower)

print(":: QUALIFYING PLAYERS ::")
print(", ".join(players_keys))
print(":: QUALIFYING PLAYER RESULTS ::")

wb = xlwt.Workbook()
ws_ps = wb.add_sheet("Player Stats")
ws_qo = wb.add_sheet("Qualified Only", cell_overwrite_ok=True)

def qualified_only(s):
    if(s["winner"] not in players_keys):
        return False
    if(s["loser"] not in players_keys):
        return False 
    return True

final_calculations(players, players_keys, ws_ps)
final_calculations(players, players_keys, ws_qo, check=qualified_only)

wb.save('player_info.xls')