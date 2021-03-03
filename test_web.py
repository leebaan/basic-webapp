from flask import Flask
import time
from webapp import create_app

def test_home_page():
    '''Function tests web application for the status code and expected output when '/' is requested'''
    web_app = create_app()

    # Create a test client using the web app configured for testing
    with web_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert response.get_data() == b'Hello World'

def test_status_alive():
    '''Function tests web application for the status code and expected output when '/status/alive' is requested'''
    web_app = create_app()

    with web_app.test_client() as test_client:
        response = test_client.get('/status/alive')
        assert response.status_code == 200
        assert response.get_data() == b''

def test_status_ready_500():
    '''Function tests web application for the status code and expected output when '/status/ready' is requested'''
    web_app = create_app()

    with web_app.test_client() as test_client:
        response = test_client.get('/status/ready')
        assert response.status_code == 500
        assert response.get_data() == b'{"ready":"false"}\n'

def test_status_ready_200():
    '''Function tests web application for the status code and expected output when '/status/ready' is requested'''
    web_app = create_app()
    time.sleep(11)

    with web_app.test_client() as test_client:
        response = test_client.get('/status/ready')
        assert response.status_code == 200
        assert response.get_data() == b'{"ready":"true"}\n'

def test_invalid_pages():
    '''Function tests web application for invalid pages and the expected output when '/whatwhowhy' is requested'''
    web_app = create_app()

    with web_app.test_client() as test_client:
        response = test_client.get('/whatwhowhy')
        assert response.status_code == 404
        assert b'does not exist' in response.get_data()
