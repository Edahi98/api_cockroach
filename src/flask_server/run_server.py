from ariadne import make_executable_schema, graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, request, jsonify, render_template
from ..flask_server.def_resolves_mutation import mutation
from .type_def_const import TYPE_DEF

shema = make_executable_schema(TYPE_DEF, mutation)

explorer_html = ExplorerGraphiQL().html(None)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        shema,
        data,
        context_value={"request": request},
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code