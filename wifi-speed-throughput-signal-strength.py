import matplotlib.pyplot as plt
import numpy as np

# Example data (replace with your actual measurements)
signal_strength = [-40, -55, -65, -75, -82]  # dBm
wifi_speed = [866, 650, 300, 150, 72]  # Mbps
throughput = [750, 500, 200, 80, 30]  # Mbps

# Create the plot
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Signal Strength (dBm)')
ax1.set_ylabel('Wi-Fi Link Speed (Mbps)', color=color)
ax1.plot(signal_strength, wifi_speed, marker='o', color=color, label='Wi-Fi Speed')
ax1.tick_params(axis='y', labelcolor=color)
ax1.invert_xaxis()  # Because higher (closer to 0) dBm means stronger

ax2 = ax1.twinx()  # second y-axis
color = 'tab:green'
ax2.set_ylabel('TCP Throughput (Mbps)', color=color)
ax2.plot(signal_strength, throughput, marker='s', color=color, label='TCP Throughput')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Wi-Fi Speed and TCP Throughput vs Signal Strength')
fig.tight_layout()
plt.grid()
plt.savefig("wifi-speed-throughput-signal-strength.png")


