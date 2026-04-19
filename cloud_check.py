import time
from core.api import get_fissures
from core.alerts import send_alert
from core.logics import time_end, match_fissure_details
from config.tracked_missions import TRACKED_MISSIONS, SP_ONLY


INTERVAL = 5  # seconds


def main():
    while True:
        try:
            fissures = get_fissures()
            for mission in TRACKED_MISSIONS:
                for fissure in fissures:
                    if SP_ONLY:
                        if fissure.get("Node")==mission["node_num"] and fissure.get("Hard"):
                            mission_type, relic_tier, sp_status = match_fissure_details(mission, fissure)

                            send_alert(f"🔥 Active fissure: {mission_type} | {relic_tier} | SP: {sp_status}\n Expire in: <t:{time_end(fissure)}:R>")
                    else:
                        if fissure.get("Node")==mission["node_num"]:
                            mission_type, relic_tier, sp_status = match_fissure_details(mission, fissure)

                            send_alert(f"🔥 Active fissure: {mission_type} | {relic_tier} | SP: {sp_status}\n Expire in: <t:{time_end(fissure)}:R>")

        except Exception as e:
            send_alert(f"⚠️ Error occurred: {e}")

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()