from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['APP_PORT'], debug=app.config['APP_DEBUG'])
