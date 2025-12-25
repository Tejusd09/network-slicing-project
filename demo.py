#!/usr/bin/env python3
"""
Network Slicing Demonstration
Shows concepts without Mininet kernel issues
"""

import time
import random

class NetworkSlice:
    def __init__(self, name, priority, color_code):
        self.name = name
        self.priority = priority
        self.color = color_code
        self.hosts = []
        
    def add_host(self, ip):
        self.hosts.append(ip)
        
    def simulate_traffic(self, duration=5):
        print(f"\n{self.color}[{self.name} SLICE]{'='*50}\033[0m")
        print(f"Priority: {self.priority}")
        print(f"Hosts: {', '.join(self.hosts)}")
        
        if "Gaming" in self.name:
            print("Traffic: Small packets, high frequency, low latency required")
            print("Use Case: League of Legends, Valorant")
            for i in range(duration):
                latency = random.randint(10, 30)
                loss = random.uniform(0, 0.1)
                print(f"  Packet {i+1}: Latency={latency}ms, Loss={loss:.2f}%")
                time.sleep(0.5)
                
        elif "Video" in self.name:
            print("Traffic: Large packets, steady stream, high bandwidth")
            print("Use Case: Netflix 4K, YouTube, Zoom")
            for i in range(duration):
                bandwidth = random.randint(15, 25)
                buffer = random.randint(10, 30)
                print(f"  Second {i+1}: {bandwidth} Mbps, Buffer={buffer}s")
                time.sleep(0.5)
                
        elif "IoT" in self.name:
            print("Traffic: Intermittent, small packets, energy efficient")
            print("Use Case: Smart sensors, home automation")
            for i in range(duration):
                if random.random() > 0.3:  # 70% chance of transmission
                    data = random.randint(10, 100)
                    print(f"  Device {i+1}: Sent {data} bytes")
                time.sleep(1)

def main():
    print("\n" + "="*60)
    print("        NETWORK SLICING DEMONSTRATION")
    print("="*60)
    
    # Create slices
    gaming = NetworkSlice("Gaming (eSports/LoL)", "HIGH", "\033[92m")  # Green
    video = NetworkSlice("Video Streaming (4K/HD)", "MEDIUM", "\033[94m")  # Blue
    iot = NetworkSlice("IoT (Smart Devices)", "LOW", "\033[93m")  # Yellow
    
    # Add hosts
    gaming.add_host("10.0.1.1")
    gaming.add_host("10.0.1.2")
    video.add_host("10.0.2.1")
    video.add_host("10.0.2.2")
    iot.add_host("10.0.3.1")
    iot.add_host("10.0.3.2")
    
    # Show topology
    print("\n\033[1mNetwork Topology Created:\033[0m")
    print("├── 🎮 Gaming Slice (VLAN 100)")
    print("│   ├── g1: 10.0.1.1")
    print("│   └── g2: 10.0.1.2")
    print("│")
    print("├── 🎥 Video Slice (VLAN 200)")
    print("│   ├── v1: 10.0.2.1")
    print("│   └── v2: 10.0.2.2")
    print("│")
    print("└── 📱 IoT Slice (VLAN 300)")
    print("    ├── i1: 10.0.3.1")
    print("    └── i2: 10.0.3.2")
    
    print("\n\033[1mQuality of Service (QoS) Configuration:\033[0m")
    print("┌─────────────────┬─────────────┬─────────────┬─────────────┐")
    print("│     Slice       │ Bandwidth   │ Max Latency │ Packet Loss │")
    print("├─────────────────┼─────────────┼─────────────┼─────────────┤")
    print("│ 🎮 Gaming       │ 100 Mbps    │ < 20ms      │ < 0.1%      │")
    print("│ 🎥 Video        │  50 Mbps    │ < 50ms      │ < 0.5%      │")
    print("│ 📱 IoT          │  10 Mbps    │ < 100ms     │ < 1%        │")
    print("└─────────────────┴─────────────┴─────────────┴─────────────┘")
    
    # Simulate traffic
    input("\nPress Enter to simulate traffic patterns...")
    
    gaming.simulate_traffic(3)
    video.simulate_traffic(3)
    iot.simulate_traffic(3)
    
    print("\n\033[1m" + "="*60)
    print("DEMONSTRATION COMPLETE")
    print("="*60 + "\033[0m")
    print("\nThis demonstrates network slicing concepts:")
    print("✅ Isolated virtual networks on shared infrastructure")
    print("✅ Different QoS for different applications")
    print("✅ Traffic prioritization (Gaming > Video > IoT)")
    print("✅ Real use cases: LoL gaming, 4K streaming, IoT devices")

if __name__ == "__main__":
    main()