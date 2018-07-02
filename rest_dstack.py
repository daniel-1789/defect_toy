

from flask import Flask, request, send_file
from flask_restful import Resource, Api, reqparse
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import threading
import io
import base64

conn = sqlite3.connect('dstack.db')
app = Flask(__name__)
api = Api(app)

df = pd.read_excel('defect_example.xlsx')
fig = plt.plot(df['Date'], df['Number_Defects'])

plt.savefig('data.png')

class PrepData(Resource):
    def get(self, file_name):
        # img = io.BytesIO()

        df = pd.read_excel('defect_example.xlsx')
        plt.plot(df['Date'], df['Number_Defects'])

        plt.savefig(file_name, format='png')
        # plot_url = base64.b64encode(img.getvalue()).decode()

        # return '<img src="data:image/png;base64,{}">'.format(plot_url)
        return 'Success!'


class DisplayData(Resource):
    """
    For a given user handle, return the 10 nearest handles with their distances
    """
    def get(self, file_name):

        return send_file(file_name, mimetype='image/png')



api.add_resource(DisplayData, '/display/<file_name>')
api.add_resource(PrepData, '/prep/<file_name>')


if __name__ == '__main__':
     app.run(port='5002')
     

