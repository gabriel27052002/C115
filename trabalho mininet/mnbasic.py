#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        # Add switches
        switches = []
        for i in range(1, 6):
            switch = self.addSwitch(f's{i}', failMode='standalone')
            switches.append(switch)

        # Add hosts
        for i in range(1, 7):
            host = self.addHost(f'h{i}', ip=f'192.168.0.{i}/28', mac=f'00:00:00:00:00:0{i}')
            self.addLink(host, switches[(i-1)//2])

def customRun():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=Controller)
    net.start()

    print('\n#### Informacoes das portas####\n\n')
    net.pingAll()

    print('\n#### Informacoes dos enderecos####\n\n')
    for host in net.hosts:
        print(f'Host: {host.name} | IP: {host.IP()} | MAC: {host.MAC()}')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customRun()


*Defini uma classe CustomTopo que herda de Topo e implementa o método build para criar a topologia da rede.
*Utilizo loops para adicionar switches e hosts de forma eficiente.
*Crio uma função customRun para iniciar a topologia personalizada, imprimir informações e permitir interação através da CLI do Mininet.
*Utilizo a função pingAll para testar a conectividade entre todos os hosts na rede.
