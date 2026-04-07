import requests
from datetime import datetime, timezone

# Official Warframe WorldState API
url = "https://api.warframe.com/cdn/worldState.php"
response = requests.get(url)
worldstate = response.json()

# Get active fissures
fissures = worldstate.get("ActiveMissions", [])

def check_fissure(SolNode, SP_Mode=True):

    for fissure in fissures:
        if SP_Mode:
            if fissure.get("Node")==SolNode and fissure.get("Hard"): #SP Only
                status = (f"{SolNode} Steel Path Active")
                time_left(SolNode, fissure)
                return (status, time_left)
        else:
            if fissure.get("Node")==SolNode: # SP+Normal Path
                status = (f"{SolNode} Active")
                time_left(SolNode, fissure)
                return (status, time_left)

        # print (mission.get("Node"), mission.get("MissionType"), mission.get("Hard"))
        # if fissure.get("Node") == "SolNode310":
        #     print ("Normal or SP")
        # if fissure.get("Node") == "SolNode310" and fissure.get("Hard"):
        #     print ("SP")
        # if fissure.get("Node") == "SolNode310" and not fissure.get("Hard"):
        #     print ("Normal")

def time_left(SolNode, fissure):

    # Get expiry time in milliseconds
    expiry_ms = int(fissure["Expiry"]["$date"]["$numberLong"])
    expiry_dt = datetime.fromtimestamp(expiry_ms / 1000, tz=timezone.utc)
    
    # Calculate time remaining
    now = datetime.now(timezone.utc)
    remaining = expiry_dt - now

    if remaining.total_seconds() > 0:
        hours, remainder = divmod(int(remaining.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{SolNode} | Time Remaining: {hours}h {minutes}m {seconds}s")

# Cascade = "SolNode232"
# if not check_fissure(Cascade):
#     print(f"No active SP Cascade")

# LithCapture = "SolNode401"
# check_fissure(LithCapture, False)

# LithExterminate = "SolNode400"
# check_fissure(LithExterminate, False)

# MesoNeoCapture = "SolNode406"
# check_fissure(MesoNeoCapture, False)

# MesoNeoExterminate = "SolNode407"
# check_fissure(MesoNeoExterminate, False)

mission_list = [
    {"mission_type": "Void Cascade", "node_num": "SolNode232"},
    {"mission_type": "Lith -- Capture", "node_num": "SolNode401"},
    {"mission_type": "Lith -- Exterminate", "node_num": "SolNode400"},
    {"mission_type": "Meso/Neo -- Capture", "node_num": "SolNode406"},
    {"mission_type": "Meso/Neo -- Exterminate", "node_num": "SolNode407"},
    {"mission_type": "Neo/Axi -- Void Survival", "node_num": "SolNode409"},
    {"mission_type": "Meso/Neo/Axi -- Void Defense", "node_num": "SolNode408"}
]

for mission in mission_list:
    if check_fissure(mission["node_num"], True) is None:
        print (f"No active {mission["mission_type"]}")

# for mission in mission_list[1:]:
#     if not check_fissure(mission["node_num"], False):
#         print(f"No active {mission["mission_type"]}")

#Mission nodes: https://wiki.warframe.com/w/World_State#Node
#Cascade = SolNode232
#Hepit (Lith Capture) = SolNode401
#Teshub (Lith Exterminate) = SolNode400
#Ukko (Meso/Neo) = SolNode406
#Oxomoco (Meso/Neo) = SolNode407
