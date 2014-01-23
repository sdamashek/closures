from twisted.words.protocols import irc
from twisted.internet import reactor, protocol

class ClosingBot(irc.IRCClient):

    nickname = "closures"
    channel = "#closures"

    def signedOn(self):
        self.join(self.channel)

    def privmsg(self, user, channel, message):
        self.data.cmd(user, message)
   
class ClosingFactory(protocol.ClientFactory):
   
    def buildProtocol(self, addr):
        import data
        p = ClosingBot()
        p.data = data.ClosingsData()
        p.data.bot = p
        return p

if __name__ == '__main__':
    f = ClosingFactory()
    reactor.connectTCP("chat.freenode.org", 6667, f)
    reactor.run()
