import time
from core.api import get_fissures
from core.alerts import send_alert
from core.logics import time_end, match_fissure_details
from config.tracked_missions import TRACKED_MISSIONS, SP_ONLY


INTERVAL = 5  # seconds


def main():

    already_alerted = set() # Store fissure_id

    while True:
        try:

            print(already_alerted)

            fissures = get_fissures()
            for mission in TRACKED_MISSIONS:
                for fissure in fissures:

                    fissure_id = f"{fissure.get("Node")}--{fissure.get("Expiry")["$date"]["$numberLong"]}" # "SolNode111--123456789"

                    if SP_ONLY:
                        if fissure.get("Node")==mission["node_num"] and fissure.get("Hard"):

                            if fissure_id not in already_alerted:

                                mission_type, relic_tier, sp_status = match_fissure_details(mission, fissure)

                                send_alert(f"🔥 Active fissure: {mission_type} | {relic_tier} | SP: {sp_status}\n Expire in: <t:{time_end(fissure)}:R>")

                                already_alerted.add(fissure_id)
                    else:
                        if fissure.get("Node")==mission["node_num"]:

                            if fissure_id not in already_alerted:

                                mission_type, relic_tier, sp_status = match_fissure_details(mission, fissure)

                                send_alert(f"🔥 Active fissure: {mission_type} | {relic_tier} | SP: {sp_status}\n Expire in: <t:{time_end(fissure)}:R>")

                                already_alerted.add(fissure_id)

        except Exception as e:
            send_alert(f"⚠️ Error occurred: {e}")

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()