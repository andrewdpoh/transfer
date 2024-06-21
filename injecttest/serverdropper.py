from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/shellcode/<exe>')
def drop_shellcode(exe):
    try: 
        fn = open(exe, 'r')
        shellcode = fn.read()
    except Exception as e: 
        print(e)
        return "not found"
    print(shellcode, type(shellcode))
    return shellcode

@app.route('/drop/<exe>')
def drop_file(exe):
    return send_file(exe)

app.run(host='0.0.0.0', port=9999, debug=True)