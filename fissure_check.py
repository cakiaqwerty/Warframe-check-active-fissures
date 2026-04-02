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
            if fissure.get("Node")==SolNode and fissure.get("Hard"):
                print (f"{SolNode} Active")
                time_left(SolNode, fissure)

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

Cascade = "SolNode232"
check_fissure(Cascade)

#Mission nodes: https://wiki.warframe.com/w/World_State#Node
#Cascade = SolNode232
#Hepit (Lith Capture) = SolNode401
#Teshub (Lith Exterminate) = SolNode400
#Ukko (Meso/Neo) = SolNode406
#Oxomoco (Meso/Neo) = SolNode407
