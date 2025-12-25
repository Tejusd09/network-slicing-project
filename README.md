# Network Slicing with Mininet
## Minimal Implementation for CSE Project

Creates 3 isolated network slices using Mininet:
1. **🎮 Gaming Slice** - For League of Legends (low latency)
2. **🎥 Video Slice** - For Netflix/YouTube (high bandwidth)
3. **📱 IoT Slice** - For smart devices (efficient)

## Quick Start

### Option 1: Use Mininet VM (Easiest)
1. Download Mininet VM: https://github.com/mininet/mininet/releases
2. Import to VirtualBox (free)
3. Copy project files to VM
4. Run: `sudo python3 slice.py`

### Option 2: Install Mininet on Ubuntu/WSL2
```bash
# Install Mininet
sudo apt-get update
sudo apt-get install mininet

# Clone and run
git clone <repo>
cd network-slice
sudo python3 slice.py