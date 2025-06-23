# import pickle
# from flask import Flask, jsonify, send_file
# import sys

# # Function to load the pickle file
# def load_pkl_file(file_path):
#     with open(file_path, 'rb') as f:
#         data = pickle.load(f)
#     return data

# # Initialize Flask app
# app = Flask(__name__)

# # Define route to serve the data
# @app.route('/data', methods=['GET'])
# def get_data():
#     try:
#         # Change the file path to your .pkl file
#         file_path = 'test_stream.pkl'
#         data = load_pkl_file(file_path)
#         return jsonify(data)  # Serves the data as JSON
#     except Exception as e:
#         return jsonify({"error": str(e)})

# # Run the app
# if __name__ == '__main__':
#     # Set the IP and port (replace with your desired values)
#     ip_address = "127.0.0.1"  # Change to specific IP if needed
#     port = 5000

#     # Run the app on the specified IP and port
#     app.run(host=ip_address, port=port, debug=True)


import pickle
import time

def load_pkl_file(file_path):
    """Load a pickle (.pkl) file."""
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

def play_pkl_data(data, delay=1):
    """
    "Play" the loaded pickle data.
    Assumes data is a list of items to display sequentially.
    
    Args:
        data: Sequential data (e.g., list of frames or time series data).
        delay: Time in seconds between frames (default: 1 second).
    """
    if isinstance(data, list):
        # If the data is a list, iterate over it
        for index, item in enumerate(data):
            print(f"Frame {index + 1}: {item}")
            time.sleep(delay)  # Wait for the specified delay time
    elif isinstance(data, dict):
        # If the data is a dictionary, iterate over its items
        for key, value in data.items():
            print(f"Key: {key}, Value: {value}")
            time.sleep(delay)  # Wait for the specified delay time
    else:
        print("Data format not recognized for playback.")

if __name__ == "__main__":
    # Specify the path to your .pkl file
    file_path = 'test_stream.pkl'
    
    # Load the pickle file
    data = load_pkl_file(file_path)
    
    # Play the data with a delay of 1 second between items
    play_pkl_data(data, delay=1)
