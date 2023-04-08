import requests

url = 'http://localhost:5000/generate-image'
data = {
    'width': 500,
    'height': 500,
    'color': 'red',
    'format': 'png'
}
response = requests.post(url, data=data)