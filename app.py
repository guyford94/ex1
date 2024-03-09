from flask import Flask

app = Flask(name)

@app.route('/')
def helloworld():
    return 'Hello, Docker!'

if name == '_main':
    app.run(debug=True, host='0.0.0.0', port=5000)
