#!/usr/bin/env python3
"""
Network Slicing - Fixed for WSL2
"""

from mininet.net import Mininet
from mininet.node import OVSSwitch, DefaultController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def createNetworkSlices():
    """Create network with 3 slices - WSL2 compatible"""
    
    # Use simpler topology to avoid WSL2 kernel issues
    net = Mininet(switch=OVSSwitch, link=TCLink)
    
    info('*** Creating Gaming Slice (LoL/Online Games)\n')
    # Gaming slice
    g_switch = net.addSwitch('s1')
    g_host1 = net.addHost('g1', ip='10.0.1.1/24')
    g_host2 = net.addHost('g2', ip='10.0.1.2/24')
    
    # Use INTEGERS for bandwidth (not strings) to avoid HTB warnings
    net.addLink(g_host1, g_switch, bw=10, delay='5ms')
    net.addLink(g_host2, g_switch, bw=10, delay='5ms')
    
    info('*** Creating Video Streaming Slice (Netflix/YouTube)\n')
    # Video slice
    v_switch = net.addSwitch('s2')
    v_server = net.addHost('v1', ip='10.0.2.1/24')
    v_client = net.addHost('v2', ip='10.0.2.2/24')
    
    net.addLink(v_server, v_switch, bw=5, delay='20ms')
    net.addLink(v_client, v_switch, bw=5, delay='20ms')
    
    info('*** Creating IoT Slice (Smart Devices)\n')
    # IoT slice
    i_switch = net.addSwitch('s3')
    i_device1 = net.addHost('i1', ip='10.0.3.1/24')
    i_device2 = net.addHost('i2', ip='10.0.3.2/24')
    
    net.addLink(i_device1, i_switch, bw=1, delay='50ms')
    net.addLink(i_device2, i_switch, bw=1, delay='50ms')
    
    # Connect slices together
    core = net.addSwitch('s0')
    net.addLink(g_switch, core)
    net.addLink(v_switch, core)
    net.addLink(i_switch, core)
    
    info('*** Starting network\n')
    net.start()
    
    # Test connectivity
    info('\n*** Testing Slices:\n')
    info('Gaming slice: g1 -> g2\n')
    net.ping([g_host1, g_host2])
    
    info('\n*** Ready!\n')
    info('Network Slices Created:\n')
    info('1. Gaming:    g1(10.0.1.1) <-> g2(10.0.1.2)\n')
    info('2. Video:     v1(10.0.2.1) <-> v2(10.0.2.2)\n')
    info('3. IoT:       i1(10.0.3.1) <-> i2(10.0.3.2)\n')
    
    # Start CLI
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetworkSlices()