#!/bin/bash
echo "Testing Mininet installation..."
sudo mn --test pingall
echo ""

echo "Testing Python files..."
python3 --version
echo ""

echo "Checking project files..."
ls -la *.py
echo ""

echo "Ready to run: sudo python3 slice.py"