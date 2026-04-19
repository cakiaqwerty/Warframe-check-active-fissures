import requests

def get_fissures():
    # Official Warframe WorldState API
    url = "https://api.warframe.com/cdn/worldState.php"
    response = requests.get(url)
    worldstate = response.json()

    # Get active fissures
    fissures = worldstate.get("ActiveMissions", [])

    return fissures