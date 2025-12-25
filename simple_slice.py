#!/usr/bin/env python3
"""
SIMPLE NETWORK SLICING - No sudo check
"""

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def createNetwork():
    """Create network with 3 slices"""
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)
    
    info('*** Creating 3 Network Slices\n')
    
    # Gaming slice
    g1 = net.addHost('g1', ip='10.0.1.1/24')
    g2 = net.addHost('g2', ip='10.0.1.2/24')
    s1 = net.addSwitch('s1')
    net.addLink(g1, s1, bw=100, delay='5ms')
    net.addLink(g2, s1, bw=100, delay='5ms')
    
    # Video slice
    v1 = net.addHost('v1', ip='10.0.2.1/24')
    v2 = net.addHost('v2', ip='10.0.2.2/24')
    s2 = net.addSwitch('s2')
    net.addLink(v1, s2, bw=50, delay='20ms')
    net.addLink(v2, s2, bw=50, delay='20ms')
    
    # IoT slice
    i1 = net.addHost('i1', ip='10.0.3.1/24')
    i2 = net.addHost('i2', ip='10.0.3.2/24')
    s3 = net.addSwitch('s3')
    net.addLink(i1, s3, bw=10, delay='50ms')
    net.addLink(i2, s3, bw=10, delay='50ms')
    
    # Core switch
    core = net.addSwitch('s0')
    net.addLink(s1, core)
    net.addLink(s2, core)
    net.addLink(s3, core)
    
    info('*** Starting network\n')
    net.start()
    
    info('\n*** Network Ready!\n')
    info('Gaming: g1(10.0.1.1) <-> g2(10.0.1.2)\n')
    info('Video:  v1(10.0.2.1) <-> v2(10.0.2.2)\n')
    info('IoT:    i1(10.0.3.1) <-> i2(10.0.3.2)\n')
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetwork()