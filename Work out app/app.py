from flask import Flask, render_template, request, jsonify
import http.client
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Muscles = request.form['Muscles']
        WorkOut = request.form['WorkOut']
        Equipment = request.form['Equipment']
        Intensity_Level = request.form['Intensity_Level']

        conn = http.client.HTTPSConnection("work-out-api1.p.rapidapi.com")
        # Replace with your actual API URL and headers
        url = "https://work-out-api1.p.rapidapi.com/search"
        headers = {
	        "X-RapidAPI-Key": "ENTER-API-KEY",
	        "X-RapidAPI-Host": "work-out-api1.p.rapidapi.com"
        }

        params = {'Muscles': Muscles, 'WorkOut': WorkOut, 'Equipment': Equipment, 'Intensity_Level': Intensity_Level}
        
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error:", response.status_code, response.text)
            data = None

        return render_template('index.html', data=data)
    
    return render_template('index.html', data=None)


if __name__ == '__main__':
    app.run(debug=True)
