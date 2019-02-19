from settings import http

if __name__ == "__main__":
	app = http.create_app()
	app.run(host="0.0.0.0", port=5555, debug=True)
