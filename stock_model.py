

from google.appengine.ext import ndb

class Stock(ndb.Model):
    name = ndb.StringProperty()
    quantity = ndb.FloatProperty()
    price = ndb.StringProperty()
    amount = ndb.FloatProperty()
    commission = ndb.FloatProperty()
    tax = ndb.FloatProperty()
    total_amount = ndb.FloatProperty()
    #percentage of investment
    poi = ndb.FloatProperty()
    actual_price = ndb.FloatProperty()
    #percentage
    profit = ndb.FloatProperty()
    price_sold = ndb.FloatProperty()
    sold_amount = ndb.FloatProperty()
    profit_money = ndb.FloatProperty()







