import time
from core.api import get_fissures
from core.alerts import send_alert
from core.logics import time_end, match_fissure_details
from config.tracked_missions import TRACKED_MISSIONS, SP_ONLY


INTERVAL = 60  # seconds


def main():

    already_alerted = {}

    while True:
        try:

            current_time_ms =  int(time.time() * 1000)
            
            expired_nodes = []

            for node, expiry_ms in already_alerted.items():

                if expiry_ms + 60000 < current_time_ms: # 60 secs buffer
                    expired_nodes.append(node)

            for node in expired_nodes:
                del already_alerted[node] # Remove expired from already_alerted
            
            fissures = get_fissures()

            for mission in TRACKED_MISSIONS:
                for fissure in fissures:

                    node = fissure.get("Node")

                    if SP_ONLY:
                        if node != mission["node_num"]:
                            continue
                        if not fissure.get("Hard"):
                            continue

                    else:
                        if node != mission["node_num"]:
                            continue
                    
                    raw_expiry_ms = int(
                        fissure["Expiry"]["$date"]["$numberLong"]
                    )

                    # Skip already alerted
                    if node in already_alerted:
                        continue
                    
                    mission_type, relic_tier, sp_status = (match_fissure_details(mission,fissure))

                    send_alert(
                        f"🔥 Active fissure: "
                        f"{mission_type} | "
                        f"{relic_tier} | "
                        f"SP: {sp_status}\n"
                        f"⏰ Expires in: "
                        f"<t:{time_end(raw_expiry_ms)}:R>"
                    )

                    already_alerted[node] = raw_expiry_ms

        except Exception as e:
            send_alert(f"⚠️ Error occurred: {e}")

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()