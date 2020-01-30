


from chalice import Chalice
import hashlib
app = Chalice(app_name='chalice_project')

@app.route('/')
def index():
    return {'response': 'ok'}

@app.route('/md5/{string_to_hash}')
def hash_it(string_to_hash):
    m = hashlib.md5()
    m.update(string_to_hash.encode("utf-8"))
    return {'response': m.hexdigest()}
