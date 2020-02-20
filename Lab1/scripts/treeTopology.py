from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import Controller
from mininet.cli import CLI
from mininet.node import CPULimitedHost


class GenericTree(Topo):
    """Simple topology example."""

    def build(self, depth=1, fanout=2):
        # Numbering:  h1..N, s1..M
        self.hostNum = 1
        self.switchNum = 1

    def build(self, depth=1, fanout=2):
        # Numbering:  h1..N, s1..M
        self.hostNum = 1
        self.switchNum = 1
        # Build topology
        self.addTree(depth, fanout)

    def addTree(self, depth, fanout):
        """Use recursion to build the generic tree."""
        isSwitch = depth > 0
        if isSwitch:
            node = self.addSwitch('s%s' % self.switchNum)
            self.switchNum += 1
            for _ in range(fanout):
                child = self.addTree(depth - 1, fanout)
                self.addLink(node, child)
        else:
            node = self.addHost('h%s' % self.hostNum)
            self.hostNum += 1
        return node


def run(a, b):
    c = Controller('c')
    net = Mininet(topo=GenericTree(depth=int(a), fanout=int(b)), host=CPULimitedHost,
                  controller=c)
    net.start()

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    a = input("Write tree depth:")
    b = input("Write the number of children:")
    run(a, b)
