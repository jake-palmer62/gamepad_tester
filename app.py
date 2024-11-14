from flask import Flask, render_template
from routes.nintendo import nintendo_bp
from routes.xbox import xbox_bp
from routes.playstation import playstation_bp

app = Flask(__name__)

app.register_blueprint(nintendo_bp)
app.register_blueprint(xbox_bp)
app.register_blueprint(playstation_bp)

@app.route('/')
@app.route('/home.html')
def home():
    featured_guides = [
        {
            'console': 'Nintendo Switch',
            'console_tag': 'nintendo',
            'title': 'Joy-Con Drift Repair',
            'description': 'Fix stick drift issues in Nintendo Switch controllers',
            'url': '/guides/switch-joycon.html'
        },
        {
            'console': 'Xbox Series X',
            'console_tag': 'xbox',
            'title': 'SSD Upgrade Guide',
            'description': 'Expand your storage with a new SSD',
            'url': '/guides/series-ssd.html'
        },
        {
            'console': 'PS5',
            'console_tag': 'playstation',
            'title': 'Fan Cleaning',
            'description': 'Maintain your PS5\'s cooling system',
            'url': '/guides/ps5-fan.html'
        },
        {
            'console': 'Xbox One',
            'console_tag': 'xbox',
            'title': 'HDMI Port Replacement',
            'description': 'Fix your display connection issues',
            'url': '/guides/xbone-hdmi.html'
        },
        {
            'console': 'Nintendo 3DS',
            'console_tag': 'nintendo',
            'title': 'Top Screen Repair',
            'description': 'Fix display issues and screen replacements',
            'url': '/guides/3ds-screen.html'
        },
        {
            'console': 'PS4',
            'console_tag': 'playstation',
            'title': 'HDD Upgrade',
            'description': 'Upgrade your PS4 storage capacity',
            'url': '/guides/ps4-hdd.html'
        },
        {
            'console': 'Xbox Series X',
            'console_tag': 'xbox',
            'title': 'Fan Replacement',
            'description': 'Fix overheating issues and noisy fans',
            'url': '/guides/series-fan.html'
        },
        {
            'console': 'Nintendo Switch',
            'console_tag': 'nintendo',
            'title': 'Battery Replacement',
            'description': 'Extend your Switch\'s battery life',
            'url': '/guides/switch-battery.html'
        }
    ]
    return render_template('home.html', featured_guides=featured_guides)

@app.route('/gamepad-tester.html')
def gamepad_tester():
    return render_template('gamepad-tester.html')

if __name__ == '__main__':
    app.run(debug=True)