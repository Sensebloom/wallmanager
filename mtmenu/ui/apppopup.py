from mtmenu.ui.popup import Popup
from mtmenu.settings import POPUP_SIZE, POPUP_POSITION
from threading import Timer


class AppPopup( Popup ):

    def __init__(self, app, **kwargs):
        self.app = app
        self.text = "Name: %s\nCategory: %s\nOwner: %s\nRuns: %s\nLikes: %s\nDislikes: %s" % (app.name, app.category, app.owner, app.runs, app.likes, app.dislikes)
        kwargs.setdefault('title', self.text)
        kwargs.setdefault('pos', (0,0))
        kwargs.setdefault('label_submit', 'Play')
        kwargs.setdefault('label_cancel', 'Cancel')
        
        self.timer = Timer(5.0, self.on_cancel)
        self.timer.start()
        super(AppPopup, self).__init__(**kwargs)

    
    def on_cancel(self):
        self.timer.cancel()
        if self.get_root_window():
            self.get_root_window().remove_widget(self)
    

    def on_submit(self):
        self.on_cancel()
        self.open_app() 
        
        
    #eu tb nao gosto de ter isto repetido x)
    def open_app(self): 
        print '\nLoading %s...\n' % unicode(self.app)
        print 'ID: %i' % self.app.id
        print '\tPath: %s\n' % self.app.get_extraction_fullpath
        print '\tBoot file: %s\n' % self.app.get_boot_file()
        self.app.execute()
