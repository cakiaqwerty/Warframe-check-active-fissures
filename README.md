# Monitor Warframe Worldstate API and Send Alert via Discord Webhook

Create .env file containing:
DISCORD_WEBHOOK_URL = <YOUR_DISCORD_WEBHOOK_API>

<YOUR_DISCORD_WEBHOOK_API> can be found at Edit Text Channel --> Integrations --> Webhook URL (Create new if needed)

# Customizable by adding preferred SolNode from https://wiki.warframe.com/w/World_State#Node to config/tracked_missions.py
## Currently have:
1. Void Cascade
2. Hepit, Void -- Fast capture + Lith/Aya
3. Teshub, Void -- Fast exterminate + Lith/Aya
4. Ukko, Void -- Fast capture + Meso/Neo/Aya
5. Oxomoco, Void -- Fast exterminate + Meso/Neo/Aya
6. Mot, Void -- Survival | Neo/Axi/Aya
7. Belenus, Void -- Defense | Neo/Axi/Aya

# Can be deployed onto Cloud Hosted VM for 24/7 Alert
