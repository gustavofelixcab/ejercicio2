

from google.appengine.ext import ndb

class Stock(ndb.Model):
    name = ndb.StringProperty()
    quantity = ndb.FloatProperty()
    price = ndb.FloatProperty()
    amount = ndb.FloatProperty()
    commission = ndb.FloatProperty()
    tax = ndb.FloatProperty()
    total_amount = ndb.FloatProperty()
    operacion = ndb.StringProperty()
#percentage of investment
    poi = ndb.FloatProperty(required=False)
    actual_price = ndb.FloatProperty(required=False)
    #percentage
    profit = ndb.FloatProperty(required=False)
    price_sold = ndb.FloatProperty(required=False)
    sold_amount = ndb.FloatProperty(required=False)
    profit_money = ndb.FloatProperty(required=False)
