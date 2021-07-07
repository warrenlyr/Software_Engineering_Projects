# Laptop Service

from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

# Instantiate the app
app = Flask(__name__)
api = Api(app)

client = MongoClient("dockerrestapi_db_1", 27017)
#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

class Laptop(Resource):
    def get(self):
        return {
            'Laptops': ['Mac OS', 'Dell', 
            'Windozzee',
	    'Yet another laptop!',
	    'Yet yet another laptop!'
            ]
        }
        
#List all
class ListAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        opentime = [item["open"] for item in items]
        closetime = [item["close"] for item in items]
        return {'Opentime':opentime, 'Closetime': closetime}
    
#List all, opentime only
class ListOpenAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        opentime = [item["open"] for item in items]
        return {'Opentime': opentime}
    
#List all, closetime only
class ListCloseAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        closetime = [item["close"] for item in items]
        return {'Closetime': closetime}
    
#List all
#use csv or json
class Timeallformat(Resource):
    def get(self,format):
        _items = db.tododb.find()
    
        if format == 'csv':
            items = [item for item in _items]
            opentime = [item["open"] for item in items]
            closetime = [item["close"] for item in items]
            open_csv = ""
            close_csv = ""
            for b in opentime:
                open_csv += b + ', '
            for a in closetime:
                close_csv += a + ', '
            return 'Opentime: '+ open_csv + ' Closetime: ' + close_csv
    
        elif format == 'json':
            items = [item for item in _items]
            opentime = [item["open"] for item in items]
            closetime = [item["close"] for item in items]
            return {'Opentime':opentime, 'Closetime': closetime}
        
#List all, opentime only
#use csv or json
class Openallformat(Resource):
    def get(self, format):
        _items = db.tododb.find()
    
        n = request.args.get('top', type = int)
        items = [item for item in _items]
    
        if  format == 'csv' :
            opentime = [item["open"] for item in items]
            if n != None:
                if n > len(items):
                    n = len(items)
                open = ""
                for i in range(n):
                    open += opentime[i] + ', '
                return open
            else:
                open = ""
                for s in opentime:
                    open += s + ', '
                return open
    
        elif format == 'json':
            if n != None:
                if n > len(items):
                    n = len(items)
                opentime = []
                for i in range(n):
                    opentime.append(items[i]['open'])
                return {'opentime': opentime}

            else:
                opentime = [item["open"] for item in items]
                return {'Opentime': opentime}
            
#List all, closetime only
#use csv or json
class Closeallformat(Resource):
    def get(self,format):
        _items = db.tododb.find()
        
        n = request.args.get('top', type = int)
        items = [item for item in _items]
    
    
        if format == 'csv':
            closetime = [item["close"] for item in items]
            if n != None:
                if n > len(items):
                    n = len(items)
                close = ""
                for i in range(n):
                    close += closetime[i]  + ', '
                return close
            else:
                close = ""
                for s in closetime:
                    close += s + ', '
                return close

        elif format == 'json':
            if n != None:
                if n > len(items):
                    n = len(items)
                closetime = []
                for i in range(n):
                    closetime.append(items[i]['close'])
                return {'Closetime': closetime}
        
            else:
                closetime = [item["close"] for item in items]
                return {'Closetime': closetime}

# Create routes
# Another way, without decorators
api.add_resource(Laptop, '/')
api.add_resource(ListAll,'/listAll')

api.add_resource(ListOpenAll,'/listOpenOnly')
api.add_resource(ListCloseAll,'/listCloseOnly')

api.add_resource(Timeallformat,'/listAll/<format>')
api.add_resource(Openallformat,'/listOpenOnly/<format>')
api.add_resource(Closeallformat,'/listCloseOnly/<format>')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
