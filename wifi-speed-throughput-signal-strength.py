import matplotlib.pyplot as plt
import numpy as np

# Example data (replace with your actual measurements)
signal_strength = [-40, -58, -74, -62, -86]  # dBm
wifi_speed = [433, 390, 195, 72.2, 14.4]  # Mbps
throughput = [289.498, 248.734, 90.288, 41.394, 10.878]  # Mbps


# Create the plot
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Signal Strength (dBm)')
ax1.set_ylabel('Wi-Fi Link Speed (Mbps)', color=color)
ax1.plot(signal_strength, wifi_speed, marker='o', color=color, label='Wi-Fi Speed')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # second y-axis
color = 'tab:green'
ax2.set_ylabel('TCP Throughput (Mbps)', color=color)
ax2.plot(signal_strength, throughput, marker='s', color=color, label='TCP Throughput')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Wi-Fi Speed and TCP Throughput vs Signal Strength')
fig.tight_layout()
plt.grid()
plt.savefig("wifi-speed-throughput-signal-strength.png")


