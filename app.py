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
    guide_content = {
        'console_tag': 'nintendo',
        'console_name': 'Nintendo Switch',
        'guide_title': 'Joy-Con Drift Fix Guide',
        'overview': '''
            <p>Joy-Con drift is a common issue where the analog stick registers movement without being touched. 
            This guide will show you how to fix drift by cleaning or replacing the joystick module.</p>
        ''',
        'tools': [
            'Y00 tri-wing screwdriver',
            'Phillips head screwdriver',
            'Compressed air',
            'Isopropyl alcohol',
            'Cotton swabs'
        ],
        'steps': [
            {
                'title': 'Remove the Joy-Con Shell',
                'content': '''
                    <p>Start by removing the 4 tri-wing screws on the back of the Joy-Con. 
                    Carefully separate the back plate from the front, being mindful of the ribbon cables inside.</p>
                ''',
                'warning': 'Be gentle with the ribbon cables as they can tear easily.'
            },
            {
                'title': 'Clean the Joystick',
                'content': '''
                    <p>Use compressed air to remove any dust around the joystick module. 
                    Apply isopropyl alcohol with a cotton swab under the rubber cap.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Drift continues after cleaning',
                'solution': 'You may need to replace the joystick module entirely.'
            },
            {
                'problem': 'Button not responding after reassembly',
                'solution': 'Check that all ribbon cables are properly reseated and locked.'
            }
        ]
    }
    return render_template('guides/guide.html', **guide_content)
@app.route('/guides/switch-battery.html')
def switch_battery():
    content = {
        'console_tag': "nintendo",
        'console_name': "Nintendo Switch",
        'guide_title': "Battery Replacement Guide",
        'overview': '''
            <p>Replace your Nintendo Switch's degraded battery to restore its original battery life. 
            This guide walks you through safely removing the old battery and installing a new one.</p>
        ''',
        'tools': [
            'Y00 tri-wing screwdriver',
            'Phillips head screwdriver',
            'Plastic pry tools',
            'Replacement battery',
            'Heat gun or hair dryer (optional)',
            'Tweezers'
        ],
        'steps': [
            {
                'title': 'Prepare Your Switch',
                'content': '''
                    <p>Power down your Switch completely and remove all accessories. 
                    Remove the Joy-Cons and microSD card if installed.</p>
                '''
            },
            {
                'title': 'Remove Back Cover',
                'content': '''
                    <p>Remove all screws from the back cover using the tri-wing screwdriver.
                    Carefully lift the back cover starting from the top corners.</p>
                ''',
                'warning': 'There are hidden clips that may break if forced.'
            },
            {
                'title': 'Disconnect and Remove Battery',
                'content': '''
                    <p>Locate the battery connector and carefully disconnect it.
                    If the battery is adhered, use gentle heat to loosen the adhesive.
                    Slowly pry up the battery using plastic tools.</p>
                ''',
                'warning': 'Never pierce or bend the battery as it may cause a fire.'
            },
            {
                'title': 'Install New Battery',
                'content': '''
                    <p>Place the new battery in the same orientation as the old one.
                    Connect the battery cable, ensuring it's fully seated.
                    Secure any adhesive strips if included with replacement.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Switch won\'t power on after replacement',
                'solution': 'Check that the battery connector is fully seated and properly oriented.'
            },
            {
                'problem': 'Battery percentage incorrect',
                'solution': 'Fully discharge and recharge the battery to calibrate it.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/switch-screen.html')
def switch_screen():
    content = {
        'console_tag': "nintendo",
        'console_name': "Nintendo Switch",
        'guide_title': "Screen Replacement Guide",
        'overview': '''
            <p>Replace a cracked or malfunctioning Nintendo Switch LCD screen. 
            This guide covers safely removing the damaged screen and installing a new one.</p>
        ''',
        'tools': [
            'Y00 tri-wing screwdriver',
            'Phillips head screwdriver',
            'Plastic pry tools',
            'Replacement LCD screen',
            'Heat gun or hair dryer',
            'Tweezers',
            'Adhesive strips'
        ],
        'steps': [
            {
                'title': 'Disassembly',
                'content': '''
                    <p>Power off the Switch and remove all accessories.
                    Remove back cover and disconnect battery for safety.</p>
                ''',
                'warning': 'Always disconnect the battery before working on the screen.'
            },
            {
                'title': 'Remove Broken Screen',
                'content': '''
                    <p>Apply heat around the edges to soften adhesive.
                    Carefully separate screen using plastic tools.
                    Keep track of all ribbon cables.</p>
                ''',
                'warning': 'Broken glass can be sharp. Use gloves if screen is cracked.'
            },
            {
                'title': 'Install New Screen',
                'content': '''
                    <p>Clean frame thoroughly of old adhesive.
                    Connect ribbon cables to new screen.
                    Apply new adhesive strips.
                    Carefully align and press screen into place.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Screen shows lines or dead pixels',
                'solution': 'Check ribbon cable connections are fully seated.'
            },
            {
                'problem': 'Touch not working',
                'solution': 'Ensure digitizer cable is properly connected.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

#3DS
@app.route('/guides/3ds-screen.html')
def ds3_screen():
    content = {
        'console_tag': "nintendo",
        'console_name': "Nintendo 3DS",
        'guide_title': "Top Screen Repair Guide",
        'overview': '''
            <p>Fix or replace a broken top screen on your Nintendo 3DS. 
            This guide covers disassembly and proper handling of ribbon cables.</p>
        ''',
        'tools': [
            'Phillips head screwdriver (#00)',
            'Tri-wing screwdriver',
            'Plastic opening tools',
            'Replacement screen',
            'Tweezers',
            'Spudger'
        ],
        'steps': [
            {
                'title': 'Initial Disassembly',
                'content': '''
                    <p>Remove SD card and battery.
                    Remove all visible screws from battery compartment and shell.</p>
                '''
            },
            {
                'title': 'Separate Shells',
                'content': '''
                    <p>Carefully separate top and bottom shells.
                    Mind the ribbon cables connecting them.</p>
                ''',
                'warning': 'Multiple ribbon cables run through the hinge. Work slowly.'
            },
            {
                'title': 'Screen Replacement',
                'content': '''
                    <p>Remove screen assembly screws.
                    Carefully disconnect and track all ribbons.
                    Install new screen in reverse order.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': '3D effect not working',
                'solution': 'Check 3D camera ribbon cable connection.'
            },
            {
                'problem': 'Screen flickering',
                'solution': 'Verify all ribbon cables are properly seated.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)
@app.route('/guides/3ds-circle.html')
def ds3_circle():
    content = {
        'console_tag': "nintendo",
        'console_name': "Nintendo 3DS",
        'guide_title': "Circle Pad Fix Guide",
        'overview': '''
            <p>Repair a loose or unresponsive Circle Pad on your Nintendo 3DS.
            Learn how to clean, calibrate, or replace the Circle Pad.</p>
        ''',
        'tools': [
            'Phillips head screwdriver (#00)',
            'Plastic opening tools',
            'Replacement Circle Pad (if needed)',
            'Isopropyl alcohol',
            'Cotton swabs'
        ],
        'steps': [
            {
                'title': 'Initial Disassembly',
                'content': '''
                    <p>Remove battery and bottom shell screws.
                    Carefully separate the shell halves.</p>
                ''',
                'warning': 'Keep track of different screw sizes and locations.'
            },
            {
                'title': 'Circle Pad Maintenance',
                'content': '''
                    <p>Clean around Circle Pad with alcohol.
                    Check for loose components.
                    Replace if mechanism is damaged.</p>
                '''
            },
            {
                'title': 'Reassembly and Testing',
                'content': '''
                    <p>Carefully reassemble shell.
                    Test Circle Pad movement.
                    Calibrate in system settings if needed.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Pad still drifting after cleaning',
                'solution': 'The sensor may need replacement if cleaning doesn\'t help.'
            },
            {
                'problem': 'Pad feels loose after repair',
                'solution': 'Check that all mounting screws are properly tightened.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/series-fan.html')
def series_fan():
    content = {
        'console_tag': "xbox",
        'console_name': "Xbox Series X/S",
        'guide_title': "Fan Replacement Guide",
        'overview': '''
            <p>Replace a noisy or malfunctioning fan in your Xbox Series X/S.
            This guide helps you safely access and install a new cooling fan.</p>
        ''',
        'tools': [
            'T8 Torx screwdriver',
            'T10 Torx screwdriver',
            'Replacement fan',
            'Plastic pry tools',
            'Thermal paste'
        ],
        'steps': [
            {
                'title': 'Console Preparation',
                'content': '''
                    <p>Unplug all cables and place on clean surface.
                    Remove side panels carefully.</p>
                ''',
                'warning': 'Opening the console voids the warranty.'
            },
            {
                'title': 'Fan Removal',
                'content': '''
                    <p>Locate the fan assembly.
                    Disconnect fan power cable.
                    Remove mounting screws.</p>
                '''
            },
            {
                'title': 'New Fan Installation',
                'content': '''
                    <p>Install new fan in same orientation.
                    Reconnect power cable.
                    Verify fan spins freely.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Fan not spinning',
                'solution': 'Check power connection and for any obstruction.'
            },
            {
                'problem': 'Excessive noise after replacement',
                'solution': 'Verify fan is properly mounted and screws are tight.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/series-ssd.html')
def series_ssd():
    content = {
        'console_tag': "xbox",
        'console_name': "Xbox Series X/S",
        'guide_title': "SSD Upgrade Guide",
        'overview': '''
            <p>Install a larger storage drive in your Xbox Series X/S.
            Learn how to properly clone and upgrade your storage.</p>
        ''',
        'tools': [
            'T8 Torx screwdriver',
            'Compatible NVMe SSD',
            'External drive for backup',
            'Thermal pad'
        ],
        'steps': [
            {
                'title': 'Data Backup',
                'content': '''
                    <p>Back up all games and saves.
                    Note down your settings.</p>
                ''',
                'warning': 'Ensure all data is backed up before proceeding.'
            },
            {
                'title': 'SSD Installation',
                'content': '''
                    <p>Remove console panels.
                    Locate storage slot.
                    Insert new SSD at correct angle.</p>
                '''
            },
            {
                'title': 'System Setup',
                'content': '''
                    <p>Format new drive.
                    Reinstall system software.
                    Restore your data.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Drive not recognized',
                'solution': 'Verify SSD is properly seated and compatible.'
            },
            {
                'problem': 'System won\'t boot',
                'solution': 'Try reinserting the drive or checking connections.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/xbone-hdmi.html')
def xbone_hdmi():
    content = {
        'console_tag': "xbox",
        'console_name': "Xbox One",
        'guide_title': "HDMI Port Repair Guide",
        'overview': '''
            <p>Replace a damaged HDMI port on your Xbox One.
            This is an advanced repair requiring soldering skills.</p>
        ''',
        'tools': [
            'Soldering iron',
            'Replacement HDMI port',
            'Flux',
            'Solder wick',
            'T8 Torx screwdriver',
            'Heat gun'
        ],
        'steps': [
            {
                'title': 'Port Access',
                'content': '''
                    <p>Disassemble console to motherboard.
                    Remove shielding around port area.</p>
                ''',
                'warning': 'Advanced soldering skills required.'
            },
            {
                'title': 'Port Removal',
                'content': '''
                    <p>Apply flux to port pins.
                    Heat and remove old port.
                    Clean pads thoroughly.</p>
                '''
            },
            {
                'title': 'New Port Installation',
                'content': '''
                    <p>Align new port carefully.
                    Solder all pins.
                    Check for bridges.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'No video output',
                'solution': 'Check for cold solder joints and bridges.'
            },
            {
                'problem': 'Poor connection',
                'solution': 'Verify port is flat against board and properly aligned.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/xbone-hdd.html')
def xbone_hdd():
    content = {
        'console_tag': "xbox",
        'console_name': "Xbox One",
        'guide_title': "HDD Replacement Guide",
        'overview': '''
            <p>Upgrade your Xbox One storage with a larger hard drive.
            Learn proper drive preparation and system recovery.</p>
        ''',
        'tools': [
            'T8 Torx screwdriver',
            'T10 Torx screwdriver',
            'New SATA hard drive',
            'USB flash drive (8GB+)',
            'Computer for drive prep'
        ],
        'steps': [
            {
                'title': 'Drive Preparation',
                'content': '''
                    <p>Format new drive properly.
                    Download system files.
                    Prepare USB recovery drive.</p>
                '''
            },
            {
                'title': 'Installation',
                'content': '''
                    <p>Open console carefully.
                    Replace old drive with new.
                    Secure in mounting bracket.</p>
                ''',
                'warning': 'Label cable orientations before disconnecting.'
            },
            {
                'title': 'System Recovery',
                'content': '''
                    <p>Use USB to reinstall system.
                    Format new drive when prompted.
                    Restore your content.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Console won\'t boot',
                'solution': 'Verify drive format and system files.'
            },
            {
                'problem': 'Drive not detected',
                'solution': 'Check SATA cable connections.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/ps5-ssd.html')
def ps5_ssd():
    content = {
        'console_tag': "playstation",
        'console_name': "PlayStation 5",
        'guide_title': "SSD Expansion Guide",
        'overview': '''
            <p>Expand your PS5 storage with an M.2 NVMe SSD.
            Learn proper installation and cooling requirements.</p>
        ''',
        'tools': [
            'Phillips head screwdriver',
            'Compatible M.2 NVMe SSD',
            'Heatsink (if not included)',
            'Clean workspace'
        ],
        'steps': [
            {
                'title': 'Console Preparation',
                'content': '''
                    <p>Power off completely.
                    Remove stand and cover.
                    Wait for cooling.</p>
                ''',
                'warning': 'Only use PS5-compatible M.2 drives.'
            },
            {
                'title': 'SSD Installation',
                'content': '''
                    <p>Remove expansion bay cover.
                    Install heatsink on SSD.
                    Insert at proper angle.</p>
                '''
            },
            {
                'title': 'System Setup',
                'content': '''
                    <p>Replace cover and power on.
                    Format new drive.
                    Verify speeds meet requirements.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Drive not recognized',
                'solution': 'Verify it meets PS5 speed requirements.'
            },
            {
                'problem': 'System runs hot',
                'solution': 'Check heatsink installation and contact.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/ps5-fan.html')
def ps5_fan():
    content = {
        'console_tag': "playstation",
        'console_name': "PlayStation 5",
        'guide_title': "Fan Cleaning Guide",
        'overview': '''
            <p>Clean your PS5's cooling system to maintain optimal performance.
            Learn how to safely access and clean the fan assembly.</p>
        ''',
        'tools': [
            'Phillips head screwdriver',
            'Compressed air',
            'Cotton swabs',
            'Isopropyl alcohol',
            'Vacuum (optional)'
        ],
        'steps': [
            {
                'title': 'Access Fan',
                'content': '''
                    <p>Remove side panels properly.
                    Locate dust collection ports.
                    Remove outer fan cover.</p>
                ''',
                'warning': 'Never spray liquid directly into console.'
            },
            {
                'title': 'Cleaning Process',
                'content': '''
                    <p>Use compressed air carefully.
                    Clean fan blades with alcohol.
                    Clear dust ports thoroughly.</p>
                '''
            },
            {
                'title': 'Reassembly',
                'content': '''
                    <p>Replace all components.
                    Verify panels click securely.
                    Test system operation.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'Fan still noisy',
                'solution': 'Check for remaining debris or loose components.'
            },
            {
                'problem': 'Console overheating',
                'solution': 'Verify airflow isn\'t blocked and vents are clear.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/ps4-hdmi.html')
def ps4_hdmi():
    content = {
        'console_tag': "playstation",
        'console_name': "PlayStation 4",
        'guide_title': "HDMI Port Replacement Guide",
        'overview': '''
            <p>Replace a damaged HDMI port on your PS4.
            This guide requires soldering experience.</p>
        ''',
        'tools': [
            'Soldering iron',
            'Replacement HDMI port',
            'Flux',
            'Solder wick',
            'T8 security bit',
            'T9 Torx'
        ],
        'steps': [
            {
                'title': 'Disassembly',
                'content': '''
                    <p>Remove power supply.
                    Access motherboard.
                    Remove port shielding.</p>
                ''',
                'warning': 'Advanced repair requiring precise soldering.'
            },
            {
                'title': 'Port Replacement',
                'content': '''
                    <p>Remove damaged port.
                    Clean pads thoroughly.
                    Install new port carefully.</p>
                '''
            },
            {
                'title': 'Testing',
                'content': '''
                    <p>Check all connections.
                    Reassemble partially.
                    Test video output.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'No display',
                'solution': 'Verify all pins are properly soldered.'
            },
            {
                'problem': 'Intermittent connection',
                'solution': 'Check for cold solder joints or bridges.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)

@app.route('/guides/ps4-hdd.html')
def ps4_hdd():
    content = {
        'console_tag': "playstation",
        'console_name': "PlayStation 4",
        'guide_title': "HDD Upgrade Guide",
        'overview': '''
            <p>Upgrade your PS4 with a larger hard drive.
            Simple process requiring no soldering.</p>
        ''',
        'tools': [
            'Phillips head screwdriver',
            'USB drive (2GB+)',
            'New 2.5" HDD/SSD',
            'Internet connection',
            'Computer'
        ],
        'steps': [
            {
                'title': 'Preparation',
                'content': '''
                    <p>Back up save data.
                    Download system software.
                    Prepare USB drive.</p>
                '''
            },
            {
                'title': 'Drive Swap',
                'content': '''
                    <p>Slide top cover off.
                    Remove drive bracket.
                    Install new drive.</p>
                ''',
                'warning': 'Back up all important data first.'
            },
            {
                'title': 'System Install',
                'content': '''
                    <p>Connect USB with system files.
                    Follow installation prompts.
                    Restore your data.</p>
                '''
            }
        ],
        'troubleshooting': [
            {
                'problem': 'PS4 won\'t recognize drive',
                'solution': 'Verify drive is properly seated and formatted.'
            }
        ]
    }
    return render_template('guides/guide.html', **content)
        
if __name__ == '__main__':
    app.run(debug=True)
            
                