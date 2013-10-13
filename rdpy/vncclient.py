'''
@author: sylvain
'''

import sys
from PyQt4 import QtGui
from rdpy.display.qt import adaptor, widget
from rdpy.protocol.rfb import rfb, factory

if __name__ == '__main__':
    #create application
    app = QtGui.QApplication(sys.argv)
    
    #add qt4 reactor
    import qt4reactor
    qt4reactor.install()
    
    #create rfb protocol
    protocol = rfb.Rfb(rfb.Rfb.CLIENT)
    w = widget.QRemoteDesktop(adaptor.RfbAdaptor(protocol))
    w.resize(1000, 700)
    w.setWindowTitle('QVNCViewer')
    w.show()
    from twisted.internet import reactor
    reactor.connectTCP("127.0.0.1", 5901, factory.RfbFactory(protocol))
    reactor.run()
    sys.exit(app.exec_())