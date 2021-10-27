class productdbrouter(object):
    route_app_labels = {'Product'}

    def db_for_read(self, model, **hints):    
        if model._meta.app_label in self.route_app_labels:
            return 'product'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels and obj2._meta.app_label in self.route_app_labels:
            return True
        elif 'Product' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db=='product'
        return 'default'

    def allow_syncdb(self, db, model):
        if db == 'product' or model._meta.app_label in self.route_app_labels:
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True
