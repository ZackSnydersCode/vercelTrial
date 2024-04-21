from flask import Flask,render_template,request,jsonify
import requests
import source


app = Flask("__main__")

@app.route("/")
def sendMain():
    return render_template("index.html")


@app.route('/fetch',methods=["POST"])
def msg():
    data = request.get_json()
    msg = data.get("msg","")
    response = get_response(msg)
    return jsonify({"res":response})
def get_response(msg):
    for que,ans in source.questions_answers.items():
        if que in msg.lower():
            return ans
    
    return render_search_engin(msg)
    
def render_search_engin(msg,chars=1300):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "titles": msg
    }
    if chars:
        params['exchars'] = chars

    response = requests.get(base_url, params=params)
    data = response.json()
    page_id = list(data['query']['pages'].keys())[0]
    if page_id == '-1':
        return "sorry"
    content = data['query']['pages'][page_id]['extract']
    print(content)
    return content



if __name__== ("__main__"):
    app.run(debug=True)