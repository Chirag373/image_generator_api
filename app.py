from flask import Flask, render_template, request, jsonify, Response
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    # Get parameters from request
    width = request.form.get('width')
    height = request.form.get('height')
    color = request.form.get('color')
    image_format = request.form.get('format')
    
    # Validate parameters
    if not width or not height or not color or not image_format:
        return jsonify({'message': 'Invalid parameters. Please provide width, height, color, and format.'}), 400
    
    try:
        width = int(width)
        height = int(height)
    except ValueError:
        return jsonify({'message': 'Width and height must be integers.'}), 400
    
    if color not in ['red', 'green', 'blue']:
        return jsonify({'message': 'Invalid color. Please choose from red, green, or blue.'}), 400
    
    if image_format not in ['jpeg', 'png', 'gif']:
        return jsonify({'message': 'Invalid format. Please choose from jpeg, png, or gif.'}), 400
    
    # Generate image array
    color_map = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0)}
    color_code = color_map[color]
    image_array = np.zeros((height, width, 3), dtype=np.uint8)
    image_array[:, :] = color_code
    
    # Encode image array to bytes
    _, image_bytes = cv2.imencode(f'.{image_format}', image_array)
    
    # Return response
    return Response(image_bytes.tobytes(), mimetype=f'image/{image_format}')

if __name__ == '__main__':
    app.run(debug=True)
