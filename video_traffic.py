#!/usr/bin/env python3
"""
Generate video streaming traffic
Simulates Netflix/YouTube traffic patterns
"""

import time
import random
import sys

def simulate_video_stream(quality="4K", duration=30):
    """Simulate video streaming traffic"""
    
    qualities = {
        "4K": {"bitrate": 25000, "buffer": 30, "codec": "H.265"},
        "1080p": {"bitrate": 8000, "buffer": 15, "codec": "H.264"},
        "720p": {"bitrate": 4000, "buffer": 10, "codec": "H.264"},
        "480p": {"bitrate": 1500, "buffer": 5, "codec": "H.264"}
    }
    
    if quality not in qualities:
        print(f"Unknown quality: {quality}")
        print(f"Available: {list(qualities.keys())}")
        return
    
    q = qualities[quality]
    
    print(f"🎥 Starting {quality} video stream")
    print(f"  Bitrate: {q['bitrate']} Kbps")
    print(f"  Buffer: {q['buffer']}s")
    print(f"  Codec: {q['codec']}\n")
    
    buffer_level = q['buffer']
    current_quality = quality
    
    for second in range(duration):
        # Simulate network conditions
        available_bandwidth = random.uniform(0.7, 1.3) * q['bitrate']
        
        # Adaptive bitrate
        if available_bandwidth < q['bitrate'] * 0.8:
            buffer_level = max(0, buffer_level - 2)
            if buffer_level < 10:
                current_quality = "720p" if quality == "4K" else "480p"
        else:
            buffer_level = min(q['buffer'], buffer_level + 1)
            if buffer_level > 20:
                current_quality = quality
        
        # Packet loss simulation
        packet_loss = random.uniform(0, 0.5)
        
        if second % 5 == 0:
            status = "🟢" if buffer_level > 10 else "🟡" if buffer_level > 5 else "🔴"
            print(f"  {status} {second}s: Buffer={buffer_level}s | "
                  f"Quality={current_quality} | Loss={packet_loss:.1f}%")
        
        time.sleep(1)
    
    print(f"\n✅ Stream completed")
    print(f"   Final quality: {current_quality}")
    print(f"   Final buffer: {buffer_level}s")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        simulate_video_stream(sys.argv[1], duration=15)
    else:
        simulate_video_stream("1080p")