from ariadne import make_executable_schema, graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, request, jsonify, render_template
from .def_resolves_mutation import mutation, query
from .type_def_const import TYPE_DEF
from random import choice

shema = make_executable_schema(TYPE_DEF, mutation, query)
explorer_html = ExplorerGraphiQL().html(None)
app = Flask(__name__)
gifs = ["https://media1.tenor.com/images/cefdf7f18976b40e53e5b3f63bbbbc8c/tenor.gif?itemid=5184402",
        "https://gifdb.com/images/high/thrilled-king-bob-big-smile-zedcdvczihwjt6fk.gif",
        "https://media0.giphy.com/media/13bjQGtqxnZxxm/200.gif?cid=790b76110j2w2q2vvaiawsdqm61p871t7cqakl1ykne0yqiq&rid=200.gif"]
@app.route("/")
def index():
    return render_template("index.html", gif=choice(gifs))

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