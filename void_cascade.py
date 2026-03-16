import requests
from datetime import datetime, timezone

# Official Warframe WorldState API
url = "https://api.warframe.com/cdn/worldState.php"
response = requests.get(url)
worldstate = response.json()

# Get active fissures
fissures = worldstate.get("ActiveMissions", [])

print("=== Steel Path Void Cascade Missions ===")

for mission in fissures:
    # Filter for Void Cascade + SP (Hard)
    if mission.get("MissionType") == "MT_VOID_CASCADE" and mission.get("Hard"): #SP Cascade
        tier = mission.get("Modifier") # T1-4: Lith, Meso, Neo, Axi #T6: Omnia
        
        # Get expiry time in milliseconds
        expiry_ms = int(mission["Expiry"]["$date"]["$numberLong"])
        expiry_dt = datetime.fromtimestamp(expiry_ms / 1000, tz=timezone.utc)
        
        # Calculate time remaining
        now = datetime.now(timezone.utc)
        remaining = expiry_dt - now
        
        # Only show missions that haven't expired yet
        if remaining.total_seconds() > 0:
            hours, remainder = divmod(int(remaining.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            print("Active")
            print(f"Void Cascade (SP Omnia) | Time Remaining: {hours}h {minutes}m {seconds}s")
            break

print("Inactive")