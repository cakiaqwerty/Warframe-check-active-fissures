from datetime import datetime, timezone

modifier_map = {
    "VoidT1": "Lith",
    "VoidT2": "Meso",
    "VoidT3": "Neo",
    "VoidT4": "Axi",
    "VoidT5": "Requiem",
    "VoidT6": "Omnia"
}

def time_end(fissure_expiry_ms):
    # Get expiry time in milliseconds
    expiry_s = int(fissure_expiry_ms) // 1000
    
    return expiry_s

def match_fissure_details(mission, fissure):
    mission_type = mission["mission_type"]
    relic_tier = modifier_map.get(fissure.get("Modifier"))
    sp_status = fissure.get("Hard")

    return mission_type, relic_tier, sp_status