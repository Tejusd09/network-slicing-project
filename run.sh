#!/bin/bash
# run.sh - Run network slicing project

echo "=========================================="
echo "   Network Slicing with Mininet"
echo "=========================================="

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root/sudo!"
    echo "Usage: sudo ./run.sh"
    exit 1
fi

echo "1. Starting Mininet network slices..."
python3 slice.py

echo "=========================================="
echo "   To test traffic generators separately:"
echo "=========================================="
echo "  For gaming traffic:"
echo "    python3 lol_traffic.py"
echo ""
echo "  For video streaming:"
echo "    python3 video_traffic.py 4K"
echo "    python3 video_traffic.py 1080p"
echo ""
echo "  For UDP flood test:"
echo "    python3 lol_traffic.py udp 10.0.1.2"
echo "=========================================="