from flask_app.app import flask_app

def main(x=0, y=0):
    fa = flask_app("doggo-dev-chart", settings="settings.json")
    fa.app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
