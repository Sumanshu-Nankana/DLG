from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class SumofNumbers(Resource):
    def get(self):
        numbers_to_add = list(range(10000001))
        n = len(numbers_to_add) - 1
        total = int(n*(n+1)/2)
        return {"total" : total}


class SumofNumbers1(Resource):
    def get(self, n):
        total = int(n*(n+1)/2)
        return {"total" : total}


api.add_resource(SumofNumbers, '/total')
api.add_resource(SumofNumbers1, '/total/<int:n>')

if __name__ == "__main__":
    app.run()
    
    
    
# curl http://127.0.0.1:5000/total
# curl localhost:5000/total/n      # where n could be any positive integer, 
                                   # i.e. upto which we need sum