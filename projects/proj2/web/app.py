from flask import Flask
from flask import abort
from flask import render_template
import os

'''
# HTTP response codes, as the strings we will actually send.
# See:  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# or    http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
##
STATUS_OK = "HTTP/1.0 200 OK\n\n"
STATUS_FORBIDDEN = "HTTP/1.0 403 Forbidden\n\n"
STATUS_NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"
STATUS_NOT_IMPLEMENTED = "HTTP/1.0 401 Not Implemented\n\n"
'''

app = Flask(__name__)

#Missing this path: waste a lot of my time
#Everything works except check for invaild symbol
#before adding path: into route
@app.route("/<path:link>")

def hello(link):
    #print(link)
    #Check for invalid symbol first,
    #Return 403 if found
    if "//" in link or ".." in link or "~" in link:
        abort(403)
    
    source_path = "templates/" + link
    #Check for file and path valid
    if os.path.isfile(source_path):
        return render_template(link)
    #return text if found, 403 if not found
    else:
        abort(404)
        
@app.errorhandler(403)
#Function to handle 403 error
#Print 403 error text, and return 403 code
def error_403(error):
    return render_template("403.html"), 403
    
@app.errorhandler(404)
#Function to handle 404 error
#Print 404 error test, and return 404 code
def error_404(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
