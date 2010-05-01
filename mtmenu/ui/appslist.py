from pymt import *
from appbutton import AppButton


class AppsList (MTKineticList):
    
    """Widget to handle applications list"""

    def __init__(self, **kwargs):
        kwargs.setdefault('title', 'Application List')
        kwargs.setdefault('size', (500,500))
        kwargs.setdefault('deletable', False)
        kwargs.setdefault('searchable', False)
        kwargs.setdefault('do_x', True)
        kwargs.setdefault('do_y', False)
        kwargs.setdefault('h_limit', 2)
        kwargs.setdefault('w_limit',0)
        kwargs.setdefault('font_size', 12)
        self.apps = None
        self.current_category = None

        super(AppsList, self).__init__(**kwargs)
        
        
    def add(self, apps):
        ''' add widgets to the applications list '''
        self.apps = self.order_by(apps, 'name')
        
        for app in self.apps:
            print app.name
            item = AppButton(app, style = {'bg-color': (0, .2, 0, 1), 'draw-background': 1})
            self.add_widget(item)
            
            
    def refresh(self, category):
        ''' replace the current list of the applications with the apps provided ''' 
        self.clear()
        self.current_category = category
        
        from utils import *
        if category:
            self.add( getApplicationsOfCategory(self.current_category) )
        else:
            self.add( getAllApplications() )
            
            
    def order_by(self, apps, str):
        return sorted(apps, key = lambda app: eval('app.'+str), reverse= True)
            
            
    def __call__(self):
        return self

