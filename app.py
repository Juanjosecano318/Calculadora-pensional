from flask import Flask, render_template
import sys
sys.path.append("src")

from view.view_web.vista_usuario import plano as blueprint_usuario

app = Flask(__name__)
app.register_blueprint(blueprint_usuario)

if __name__ == '__main__':
    app.run(debug=True)










