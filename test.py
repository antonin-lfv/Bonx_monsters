import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

ratio_common_attack = 200
ratio_common_defense = 1050
ratio_rare_attack = 400
ratio_rare_defense = 1250
ratio_epic_attack = 600
ratio_epic_defense = 1450
ratio_legendary_attack = 1000
ratio_legendary_defense = 1850
common_defense_evolution = (np.sqrt(np.arange(0, 200))*ratio_common_defense+70)
common_attack_evolution = (np.sqrt(np.arange(0, 200))*ratio_common_attack+40)
rare_defense_evolution = (np.sqrt(np.arange(0, 200))*ratio_rare_defense+90)
rare_attack_evolution = (np.sqrt(np.arange(0, 200))*ratio_rare_attack+50)
epic_defense_evolution = (np.sqrt(np.arange(0, 200))*ratio_epic_defense+110)
epic_attack_evolution = (np.sqrt(np.arange(0, 200))*ratio_epic_attack+60)
legendary_defense_evolution = (np.sqrt(np.arange(0, 200))*ratio_legendary_defense+150)
legendary_attack_evolution = (np.sqrt(np.arange(0, 200))*ratio_legendary_attack+80)

common_power_evolution = [100]
rare_power_evolution = [200]
epic_power_evolution = [300]
legendary_power_evolution = [500]

for level in range(2, 201):
    common_power_evolution.append(common_power_evolution[0] * level)
    rare_power_evolution.append(rare_power_evolution[0] * level)
    epic_power_evolution.append(epic_power_evolution[0] * level)
    legendary_power_evolution.append(legendary_power_evolution[0] * level)

fig = go.Figure()
fig.add_trace(go.Scatter(x=list(range(1, 201)), y=common_defense_evolution, name="Common Defense"))
fig.add_trace(go.Scatter(x=list(range(1, 201)), y=common_attack_evolution, name="Common Attack"))
# fig.add_trace(go.Scatter(x=list(range(1, 201)), y=common_power_evolution, name="Common Power"))
fig.add_trace(go.Scatter(x=list(range(1, 201)), y=rare_defense_evolution, name="Rare Defense"))
fig.add_trace(go.Scatter(x=list(range(1, 201)), y=rare_attack_evolution, name="Rare Attack"))
# fig.add_trace(go.Scatter(x=list(range(1, 201)), y=rare_power_evolution, name="Rare Power"))
fig.add_trace(go.Scatter(x=list(range(1, 201)), y=epic_defense_evolution, name="Epic Defense"))
fig.add_trace(go.Scatter(x=list(range(1, 201)), y=epic_attack_evolution, name="Epic Attack"))
# fig.add_trace(go.Scatter(x=list(range(1, 201)), y=epic_power_evolution, name="Epic Power"))
fig.add_trace(go.Scatter(x=list(range(1, 201)), y=legendary_defense_evolution, name="Legendary Defense"))
fig.add_trace(go.Scatter(x=list(range(1, 201)), y=legendary_attack_evolution, name="Legendary Attack"))
# fig.add_trace(go.Scatter(x=list(range(1, 201)), y=legendary_power_evolution, name="Legendary Power"))

fig.update_layout(
    title="Evolution of the defense, attack and power of the monsters",
    xaxis_title="Level",
    yaxis_title="Value",
    legend_title="Legend",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

plot(fig)
