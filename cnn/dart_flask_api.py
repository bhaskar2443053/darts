
from train_search_flask import *

args=init_model()
#start_train(args)

#import sys
#sys.path.append('/l/users/bhaskar.rao/work/projects/hospital/darts/')
#print(sys.path)

from flask import Flask, jsonify
from flask_cors import CORS

#import logging


app = Flask(__name__, static_url_path='/upload', static_folder='upload')#args.save)


CORS(app, supports_credentials=True)

save_root_path = args.save





@app.route('/')
def index_method():
    # txtwriter = open('upload/log.txt', 'w', buffering=1)
    # start_training(args, model, device, train_loader, test_loader, optimizer, scheduler, txtwriter)
    # txtwriter.close()
    return jsonify({'result': 'test success'})


@app.route('/execute', methods=['GET'])
def execute():
    try:
        #txtwriter = open('upload/log.txt', 'w', buffering=1)
        start_train(args)
        #txtwriter.close()
        return jsonify({'training': True})
    except Exception as err:
        #logging.info('error: %s', err)
        return jsonify({'training': False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)