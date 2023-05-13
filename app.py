from flask import render_template
import connexion
import exceptions


def not_found_handler(error):
    return {
        "detail": str(error),
        "status": 404,
        "title": "Not Found",
        "type": "not_found",
        "method": "get"
    }, 404


def bad_request_handler(error):
    return {
        "detail": str(error),
        "status": 400,
        "title": "Bad Request",
        "type": "invalid_request",
        "method": "get"
    }, 400


app = connexion.App(__name__, specification_dir="./")

app.add_error_handler(exceptions.NotFoundException, not_found_handler)
app.add_error_handler(exceptions.BadRequestException, bad_request_handler)
app.add_api("swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
