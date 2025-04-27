import matplotlib.pyplot as plt

# Distance as category numbers (not meters)
distance = [1, 2, 3, 4, 5]  # 1=Very Close, 2-4=Intermediate, 5=Far
signal_strength = [-40, -55, -65, -75, -82]  # dBm (example)
wifi_speed = [866, 650, 300, 150, 72]  # Mbps (example)


signal_strength.sort(reverse=False)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Distance to AP')
ax1.set_ylabel('Signal Strength (dBm)', color=color)
ax1.plot(distance, signal_strength, marker='o', color=color, label='Signal Strength')
ax1.tick_params(axis='y', labelcolor=color)
ax1.invert_yaxis()

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Wi-Fi Link Speed (Mbps)', color=color)
ax2.plot(distance, wifi_speed, marker='s', color=color, label='Wi-Fi Speed')
ax2.tick_params(axis='y', labelcolor=color)

# Set custom x-axis labels
ax1.set_xticks([1, 2, 3, 4, 5])
ax1.set_xticklabels(['Very Close (1)', 'Intermediate (2)', 'Intermediate (3)', 'Intermediate (4)', 'Far (5)'])

plt.title('Signal Strength and Wi-Fi Speed vs Distance from AP')
fig.tight_layout()
plt.grid()
plt.savefig("signal_strength_wifi_speed_distance.png")
