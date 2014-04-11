from Cocoa import *
from MyWindowController import *

class AppDelegate (NSObject):
    u"""
    Delegate is the main logic component, which sets the controllers.
    """
    myWindowController = objc.ivar()

    @objc.IBAction
    def newDocument_(self, sender):
        if self.myWindowController is None:
            self.myWindowController = MyWindowController.alloc().initWithWindowNibName_("TestWindow")

        self.myWindowController.showWindow_(self)


    def applicationDidFinishLaunching_(self, notification):
        u"""
        Open a new document after application launch.
        """
        self.newDocument_(self)

    def validateMenuItem_(self, theMenuItem):
        enable = self.respondsToSelector_(theMenuItem.action())

        # disable "New" if the window is already up
        if theMenuItem.action() == 'newDocument:':
            if self.myWindowController.window().isKeyWindow():
                enable = False

        return enable
