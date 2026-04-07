import requests
from datetime import datetime, timezone

# Official Warframe WorldState API
url = "https://api.warframe.com/cdn/worldState.php"
response = requests.get(url)
worldstate = response.json()

# Get active fissures
fissures = worldstate.get("ActiveMissions", [])

modifier_map = {
    "VoidT1": "Lith",
    "VoidT2": "Meso",
    "VoidT3": "Neo",
    "VoidT4": "Axi",
    "VoidT5": "Requiem",
    "VoidT6": "Omnia"
}

# Init
mission_list = [
    {"mission_type": "Void Cascade", "node_num": "SolNode232"},
    {"mission_type": "Lith Capture", "node_num": "SolNode401"},
    {"mission_type": "Lith Exterminate", "node_num": "SolNode400"},
    {"mission_type": "Meso/Neo Capture", "node_num": "SolNode406"},
    {"mission_type": "Meso/Neo Exterminate", "node_num": "SolNode407"},
    {"mission_type": "Neo/Axi Void Survival", "node_num": "SolNode409"},
    {"mission_type": "Meso/Neo/Axi Void Defense", "node_num": "SolNode408"}
]

sp_only = False

# Functions

def check_fissure(mission, SP_Mode=True):

    for fissure in fissures:

        if SP_Mode:
        #SP Only
            if fissure.get("Node")==mission["node_num"] and fissure.get("Hard"):
                mission_status = (mission["mission_type"])
                time_left = check_time_left(mission["node_num"], fissure)
                relic_tier = fissure.get("Modifier")
                sp_status = fissure.get("Hard")
                return (mission_status, time_left, relic_tier, sp_status)
        
        else:
        #SP + Normal Path
            if fissure.get("Node")==mission["node_num"]:
                mission_status = (mission["mission_type"])
                time_left = check_time_left(mission["node_num"], fissure)
                relic_tier = fissure.get("Modifier")
                sp_status = fissure.get("Hard")
                return (mission_status, time_left, relic_tier, sp_status)
            
    return mission["mission_type"], None, None, None

        # print (mission.get("Node"), mission.get("MissionType"), mission.get("Hard"))
        # if fissure.get("Node") == "SolNode310":
        #     print ("Normal or SP")
        # if fissure.get("Node") == "SolNode310" and fissure.get("Hard"):
        #     print ("SP")
        # if fissure.get("Node") == "SolNode310" and not fissure.get("Hard"):
        #     print ("Normal")

def check_time_left(SolNode, fissure):

    # Get expiry time in milliseconds
    expiry_ms = int(fissure["Expiry"]["$date"]["$numberLong"])
    expiry_dt = datetime.fromtimestamp(expiry_ms / 1000, tz=timezone.utc)
    
    # Calculate time remaining
    now = datetime.now(timezone.utc)
    remaining = expiry_dt - now

    if remaining.total_seconds() > 0:
        hours, remainder = divmod(int(remaining.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        return (f"Time Remaining: {hours}h {minutes}m {seconds}s")

# Main START
if sp_only:
    print ("================== SP ONLY ==================")
else:
    print ("================== NORMAL + SP ==================")
for mission in mission_list:
    mission_type, time_left, relic_tier, sp_status = check_fissure(mission, sp_only)
    if time_left is None:
        print (f"No active {mission_type}")
    else:
        print(f"{mission_type} | {time_left} | {modifier_map.get(relic_tier)} | SP: {sp_status}")

#Mission nodes: https://wiki.warframe.com/w/World_State#Node
#Cascade = SolNode232
#Hepit (Lith Capture) = SolNode401
#Teshub (Lith Exterminate) = SolNode400
#Ukko (Meso/Neo) = SolNode406
#Oxomoco (Meso/Neo) = SolNode407
