from pymt import *
from utils import *
from ui import apps_grid


class CategoryButton( MTKineticItem ):

    def __init__( self, cat, **kwargs ):
        self.category = cat
        if cat:
            kwargs.setdefault('label', cat.name)
        else:
            kwargs.setdefault('label', 'All')
        kwargs.setdefault('size', (120,40))
        kwargs.setdefault('font_size', 12)
        kwargs.setdefault('deletable', False)
        super(CategoryButton, self).__init__(**kwargs)



    def on_press( self, touch ):
        print self.category
        if self.category:
            apps_grid.replace( getApplicationsOfCategory(self.category) )
        else:
            apps_grid.replace( getAllApplications() )
        

    def on_release( self, touch ):
        return
