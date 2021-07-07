import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import arrow
import flask
import logging
import acp_times
import config
from flask_restful import Resource, Api

app = Flask(__name__)
CONFIG = config.configuration()
api = Api(app)

client = MongoClient("dockerrestapi_db_1", 27017)
#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

@app.route('/')
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

@app.route('/display', methods = ['POST'])
def todo():
    
    _items = db.tododb.find()
    items = [item for item in _items]
    
    
    return render_template('todo.html', items = items)

@app.route('/submit', methods=['POST'])
def new():
    # Clean up
    db.tododb.drop()

    # Read from input file
    km = request.form.getlist('km')
    distance = request.form.getlist('distance')
    open = request.form.getlist('open')
    close = request.form.getlist('close')
    
    app.logger.debug("km={}".format(km))
    app.logger.debug("distance={}".format(distance))
    app.logger.debug("open={}".format(open))
    app.logger.debug("close={}".format(close))
    
    # Check if it's empty first
    if km != None and distance != None and open != None and close != None:
        i = 0
        while i < len(km):
            app.logger.debug("km[1]={}".format(km[1]))
            if str(km[i])!= ""  and str(open[i])!= "" and str(close[i])!= "":
                item_doc = {'km': str(km[i]), 'distance': str(distance), 'open' : str(open[i]), 'close' : str(close[i])}#formate
                db.tododb.insert(item_doc)
            i += 1
    else:
        # Return 404 if it's empty
        return redirect(url_for(404))

    # Return to main page if success
    return redirect(url_for('index'))

@app.route("/_calc_times")
def _calc_times():
    """
        Calculates open/close times from miles, using rules
        described at https://rusa.org/octime_alg.html.
        Expects one URL-encoded argument, the number of miles.
        """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type = float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    
    # Read
    start_date = request.args.get('begin_date',"",type = str)
    start_time = request.args.get('begin_time',"", type = str)
    brevet_dist = request.args.get('brevet_dist' ,999 , type = int)
    # Format
    time_format = (start_date + 'T' + start_time+":00.000000-08:00")
    time = arrow.get(time_format)
    # Error if it exceed 20%
    if (km > (brevet_dist * 1.2)):
        result  = {"open" : "Error", "close": "Error"}
    else:
        open_time = acp_times.open_time(km, brevet_dist, time)
        close_time = acp_times.close_time(km, brevet_dist, time)
        result = {"open": open_time, "close": close_time}
    
    return flask.jsonify(result=result)
    
#===NEW ADDED===
class Laptop(Resource):
    def get(self):
        return {
            'Laptops': ['Mac OS', 'Dell',
            'Windozzee',
        'Yet another laptop!',
        'Yet yet another laptop!'
            ]
    }
    
#List all function
#List all opentime and closetime
class ListAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        opentime = [item["open"] for item in items]
        closetime = [item["close"] for item in items]
        return {'Opentime':opentime, 'Closetime': closetime}
    
#List all, opentime
class ListOpenAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        opentime = [item["open"] for item in items]
        return {'Opentime': opentime}

#List all, closetime
class ListCloseAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        closetime = [item["close"] for item in items]
        return {'Closetime': closetime}
    
#List all,
#use csv or jason
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
        
#List all, opentime
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
            
#List all, opentime
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

#Add required link
api.add_resource(Laptop, '/')
api.add_resource(ListAll,'/listAll')
api.add_resource(ListOpenAll,'/listOpenOnly')
api.add_resource(ListCloseAll,'/listCloseOnly')
api.add_resource(Timeallformat,'/listAll/<format>')
api.add_resource(Openallformat,'/listOpenOnly/<format>')
api.add_resource(Closeallformat,'/listCloseOnly/<format>')

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
