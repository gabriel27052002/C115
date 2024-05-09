from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add hosts
        hosts = []
        for i in range(1, 7):
            host = self.addHost(f'h{i}', ip=f'192.168.0.{i}/28', mac=f'00:00:00:00:00:0{i}')
            hosts.append(host)

        # Add switches
        switches = []
        for i in range(1, 6):
            switch = self.addSwitch(f's{i}', failMode='standalone')
            switches.append(switch)

        # Add links
        for i in range(0, 5):
            self.addLink(hosts[i], switches[i//2])
        self.addLink(hosts[4], switches[2])
        self.addLink(hosts[5], switches[2])
        self.addLink(hosts[3], switches[3])
        self.addLink(hosts[2], switches[3])
        self.addLink(hosts[1], switches[4])
        self.addLink(hosts[0], switches[4])

topos = {'mytopo': MyTopo}


Utilizo loops para adicionar os hosts e switches.