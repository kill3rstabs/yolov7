from flask import * 
import object_tracker
app = Flask(__name__)
@app.route('/')
def helloWorld():
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        print("hi")
        # sys.argv = []
        f.save('static/'+f.filename)
        
        object_tracker.main('./static/'+f.filename)
        return redirect("/endpoint")
        
@app.route('/endpoint',methods= ['GET','POST'])
def endpoint():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)