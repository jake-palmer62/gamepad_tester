# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Main routes
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
            'console': 'Xbox One',
            'console_tag': 'xbox',
            'title': 'HDMI Port Replacement',
            'description': 'Fix your display connection issues',
            'url': '/guides/xbone-hdmi.html'
        },
        {
            'console': 'Xbox One',
            'console_tag': 'xbox',
            'title': 'HDMI Port Replacement',
            'description': 'Fix your display connection issues',
            'url': '/guides/xbone-hdmi.html'
        }
    ]
    return render_template('home.html', featured_guides=featured_guides)

@app.route('/gamepad-tester.html')
def gamepad_tester():
    return render_template('gamepad-tester.html')

# Nintendo Switch guides
@app.route('/guides/switch-joycon.html')
def switch_joycon():
    return render_template('guides/guide.html',
                         console_tag="nintendo",
                         console_name="Nintendo Switch",
                         guide_title="Joy-Con Drift Fix Guide")

@app.route('/guides/switch-battery.html')
def switch_battery():
    return render_template('guides/guide.html',
                         console_tag="nintendo",
                         console_name="Nintendo Switch",
                         guide_title="Battery Replacement Guide")

@app.route('/guides/switch-screen.html')
def switch_screen():
    return render_template('guides/guide.html',
                         console_tag="nintendo",
                         console_name="Nintendo Switch",
                         guide_title="Screen Replacement Guide")

# 3DS guides
@app.route('/guides/3ds-screen.html')
def ds3_screen():
    return render_template('guides/guide.html',
                         console_tag="nintendo",
                         console_name="Nintendo 3DS",
                         guide_title="Top Screen Repair Guide")

@app.route('/guides/3ds-circle.html')
def ds3_circle():
    return render_template('guides/guide.html',
                         console_tag="nintendo",
                         console_name="Nintendo 3DS",
                         guide_title="Circle Pad Fix Guide")

# Xbox Series X/S guides
@app.route('/guides/series-fan.html')
def series_fan():
    return render_template('guides/guide.html',
                         console_tag="xbox",
                         console_name="Xbox Series X/S",
                         guide_title="Fan Replacement Guide")

@app.route('/guides/series-ssd.html')
def series_ssd():
    return render_template('guides/guide.html',
                         console_tag="xbox",
                         console_name="Xbox Series X/S",
                         guide_title="SSD Upgrade Guide")

# Xbox One guides
@app.route('/guides/xbone-hdmi.html')
def xbone_hdmi():
    return render_template('guides/guide.html',
                         console_tag="xbox",
                         console_name="Xbox One",
                         guide_title="HDMI Port Repair Guide")

@app.route('/guides/xbone-hdd.html')
def xbone_hdd():
    return render_template('guides/guide.html',
                         console_tag="xbox",
                         console_name="Xbox One",
                         guide_title="HDD Replacement Guide")

# PS5 guides
@app.route('/guides/ps5-ssd.html')
def ps5_ssd():
    return render_template('guides/guide.html',
                         console_tag="playstation",
                         console_name="PlayStation 5",
                         guide_title="SSD Expansion Guide")

@app.route('/guides/ps5-fan.html')
def ps5_fan():
    return render_template('guides/guide.html',
                         console_tag="playstation",
                         console_name="PlayStation 5",
                         guide_title="Fan Cleaning Guide")

# PS4 guides
@app.route('/guides/ps4-hdmi.html')
def ps4_hdmi():
    return render_template('guides/guide.html',
                         console_tag="playstation",
                         console_name="PlayStation 4",
                         guide_title="HDMI Port Fix Guide")

@app.route('/guides/ps4-hdd.html')
def ps4_hdd():
    return render_template('guides/guide.html',
                         console_tag="playstation",
                         console_name="PlayStation 4",
                         guide_title="HDD Upgrade Guide")

if __name__ == '__main__':
    app.run(debug=True)