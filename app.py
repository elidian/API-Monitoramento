from api import app, db
from api.models.user import User
from api.models.cam import Cam

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Cam': Cam}

if __name__ == '__main__':
    app.run(debug=True)
