from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from knapsack_problem_solver import solve_knapsack_problem

app = Flask(__name__)
api = Api()

CORS(app, supports_credentials=True)

class Main(Resource):
    def post(self):

        knapsack_problem = request.json
        solution, weight, fitnes = solve_knapsack_problem(knapsack_problem)
        
        response = {"items": solution, "fitnes": fitnes, "weight": weight}

        return response, 200


api.add_resource(Main, "/api/main")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")