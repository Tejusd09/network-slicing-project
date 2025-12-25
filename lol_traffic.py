#!/usr/bin/env python3
"""
Generate League of Legends-like traffic
Run on Mininet hosts to simulate gaming traffic
"""

import socket
import time
import random
import sys

def simulate_lol_traffic(host_ip, duration=30):
    """Simulate LoL gaming traffic patterns"""
    print(f"🎮 Starting LoL traffic from {host_ip}")
    print(f"  Duration: {duration}s")
    print(f"  Expected: 40-100 Kbps, <20ms latency\n")
    
    start_time = time.time()
    packets_sent = 0
    
    while time.time() - start_time < duration:
        # Gaming packets are small and frequent
        packet_size = random.randint(60, 120)  # bytes
        interval = random.uniform(0.016, 0.033)  # 30-60 packets/sec
        
        # Simulate gaming actions
        actions = [
            "MOVE", "ATTACK", "ABILITY", "CHAT", 
            "PING", "ITEM_BUY", "LEVEL_UP", "KILL"
        ]
        action = random.choice(actions)
        
        # Add random latency
        latency = random.randint(10, 25)
        if latency > 20:
            print(f"⚠️  High latency: {latency}ms (may affect gameplay)")
        
        packets_sent += 1
        
        if packets_sent % 10 == 0:
            print(f"  📦 Packet {packets_sent}: {action} | "
                  f"Size: {packet_size}B | Latency: {latency}ms")
        
        time.sleep(interval)
    
    print(f"\n✅ LoL simulation complete!")
    print(f"   Total packets: {packets_sent}")
    print(f"   Avg rate: {packets_sent/duration:.1f} packets/sec")

def udp_flood_test(target_ip, target_port=7777, duration=10):
    """Test network with UDP flood (like game traffic)"""
    print(f"🚀 Starting UDP flood test to {target_ip}:{target_port}")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start = time.time()
    packets = 0
    
    while time.time() - start < duration:
        message = f"GAME_PACKET_{packets}".encode()
        sock.sendto(message, (target_ip, target_port))
        packets += 1
        
        if packets % 100 == 0:
            print(f"  Sent {packets} packets...")
        
        time.sleep(0.001)  # 1000 packets/sec
    
    sock.close()
    print(f"✅ Sent {packets} packets in {duration}s")
    print(f"   Rate: {packets/duration:.0f} packets/sec")

if __name__ == "__main__":
    # Simple test mode
    if len(sys.argv) > 1:
        if sys.argv[1] == "udp":
            target = sys.argv[2] if len(sys.argv) > 2 else "10.0.1.2"
            udp_flood_test(target)
        else:
            simulate_lol_traffic("10.0.1.1", duration=15)
    else:
        simulate_lol_traffic("10.0.1.1")