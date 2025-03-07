from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/games', methods=['GET'])
def get_games():
    games = [
        {"id": "1", "title": "Temple Run", "url": "https://poki.com/en/g/temple-run-2"}
    ]
    return jsonify({"status": "success", "games": games})

@app.route('/api/start_game', methods=['POST'])
def start_game():
    try:
        game_id = request.json.get('game_id')
        if game_id == "1":
            return jsonify({
                "status": "success",
                "message": "Temple Run launched",
                "game_url": "https://poki.com/en/g/temple-run-2"
            })
        return jsonify({"status": "error", "message": "Invalid game ID"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)