# builtin imports
import os

# 3rd party imports
from flask import Flask, request, redirect



# Create the app
app = Flask(__name__)



# Define the routes
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')



# Main execution loop
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


