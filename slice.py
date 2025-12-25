##!/usr/bin/env python3
"""
Minimal Network Slicing - No QoS
"""

from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

net = Mininet(switch=OVSSwitch)

# Add hosts
g1 = net.addHost('g1', ip='10.0.1.1/24')
g2 = net.addHost('g2', ip='10.0.1.2/24')
v1 = net.addHost('v1', ip='10.0.2.1/24')
v2 = net.addHost('v2', ip='10.0.2.2/24')
i1 = net.addHost('i1', ip='10.0.3.1/24')
i2 = net.addHost('i2', ip='10.0.3.2/24')

# Add switches
s1 = net.addSwitch('s1')  # Gaming
s2 = net.addSwitch('s2')  # Video
s3 = net.addSwitch('s3')  # IoT
core = net.addSwitch('s0')  # Core

# Connect hosts to switches
net.addLink(g1, s1)
net.addLink(g2, s1)
net.addLink(v1, s2)
net.addLink(v2, s2)
net.addLink(i1, s3)
net.addLink(i2, s3)

# Connect switches to core
net.addLink(s1, core)
net.addLink(s2, core)
net.addLink(s3, core)

# Start network
net.start()

print("\n" + "="*60)
print("NETWORK SLICES CREATED!")
print("="*60)
print("🎮 Gaming Slice:   g1(10.0.1.1)  <->  g2(10.0.1.2)")
print("🎥 Video Slice:    v1(10.0.2.1)  <->  v2(10.0.2.2)")
print("📱 IoT Slice:      i1(10.0.3.1)  <->  i2(10.0.3.2)")
print("="*60)
print("\nTest commands in Mininet CLI:")
print("  g1 ping g2    # Test gaming slice")
print("  v1 ping v2    # Test video slice")
print("  nodes         # Show all devices")
print("  exit          # Quit")
print("="*60 + "\n")

CLI(net)
net.stop()