from flask import Blueprint, render_template, request

nintendo_bp = Blueprint('nintendo', __name__)

@nintendo_bp.route('/guides/switch-joycon.html')
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

@nintendo_bp.route('/guides/switch-battery.html')
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

@nintendo_bp.route('/guides/switch-screen.html')
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

@nintendo_bp.route('/guides/3ds-screen.html')
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

@nintendo_bp.route('/guides/3ds-circle.html')
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

@nintendo_bp.route('/guides/switch-serial.html', methods=['GET', 'POST'])
def switch_serial():
    result = None
    serial = None
    
    if request.method == 'POST':
        serial = request.form.get('serial', '').strip()
        if serial:
            # XAW1: Original Switch model
            if serial.startswith('XAW1'):
                number = int(serial[6:8])
                if number < 10:
                    result = "Unpatched - This console can be modded"
                elif number < 40:
                    result = "Possibly patched - Would need additional verification"
                else:
                    result = "Patched - This console cannot be modded"
            # XAW4 and newer are always patched
            elif serial.startswith(('XAW4', 'XAW7', 'XAJ1', 'XAJ4', 'XAJ7')):
                result = "Patched - This console cannot be modded"
            else:
                result = "Unknown serial format - Please verify the serial number"

    content = {
        'console_tag': "nintendo",
        'console_name': "Nintendo Switch",
        'guide_title': "Serial Number Checker",
        'overview': '''
            <p>Check if your Nintendo Switch is patched or unpatched based on the serial number.
            This can help determine your console's compatibility with certain modifications.</p>
        ''',
        'serial': serial,
        'result': result
    }
    return render_template('guides/switch-serial.html', **content)