from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.Redis(
    host='redis',
    port=6379,
    password='supersecret',
    decode_responses=True
)

@app.route('/api/users')
def users():
    cache.incr('api_calls')
    return jsonify({
        'users': ['alice', 'bob'],
        'calls': int(cache.get('api_calls'))
    })

@app.route('/api/secret')
def secret():
    cache.set('admin_token', 'eyJhbGciOiJIUzI1NiJ9.admin.secret')
    return jsonify({'status': 'token cached'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)