from flask import Blueprint, render_template, request

nintendo_bp = Blueprint('nintendo', __name__)
################################################ Nintendo Switch ################################################
@nintendo_bp.route('/guides/switch_disassembly.html')
def switch_disassembly():
    guide_content = {
        'console_tag': 'nintendo',
        'console_name': 'Nintendo Switch',
        'guide_title': 'Nintendo Switch Console Disassembly',
        'overview': '''
            <p>This guide will walk you through safely disassembling your Nintendo Switch console. 
            Whether you need to clean the internal components, replace the cooling fan, or replace parts such as the game card slot.
            </p>
        ''',
        'tools': [
            'Y00 tri-wing screwdriver',
            'Phillips head screwdriver #00',
            'Plastic pry tool',
            'Spudger or plastic opening tool',
            'Tweezers',
            'Small container for screws',
            'Isopropyl Alcohol (99%)',
            'Q-Tips',
            'Thermal Paste (for reassemmbly)'
        ],
        'steps': [
            {
                'title': 'Prepare Your Workspace',
                'content': '''
                    <p>Power off your Switch completely by holding the power button for 12 seconds.
                    Remove both Joy-Con controllers from the sides of the console. Remove any game cards and sd cards if they are inserted.
                    Set up your workspace with a clean, well-lit, static-free surface. Lay out a soft mat or cloth to protect the screen.</p>
                '''
            },
            {
                 'title': 'Remove Corner Screws',
                'content': '''
                    <p>Using your Y00 tri-wing screwdriver, remove the four tri-wing screws located in each corner
                    of the back cover. Place these screws your container and keep them separate from the other screws.</p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step2.jpg" alt="Corner screw locations">
                    </div>
                '''                
            },
            {
                'title': 'Remove Kickstand Screw',
                'content': '''
                    <p>Open the kickstand on the back of the console. Inside, you'll find a PH00 screw.
                    Remove this screws using your Phillips screwdriver and store them separately.</p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step3.jpg" alt="Corner screw locations">
                    </div>
                '''
            },
            {
                'title': 'Remove Additional Screws',
                'content': '''
                    <p>Locate and remove the remaining PH00 screws: one on the top of the console,
                    two on the bottom, and one in the middle of each Joy-Con rail.</p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step4-1.jpg" alt="Corner screw locations">
                    </div>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step4-2.jpg" alt="Corner screw locations">
                    </div>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step4-3.jpg" alt="Corner screw locations">
                    </div>
                ''',
                'warning': "In order to prevent these screws from stripping, apply firm downward force."
            },
            {
                'title': 'Remove Back Cover',
                'content': '''
                    <p>Once all screws are removed, carefully lift the back cover away from the console.
                    The cover should come off without much resistance. Set it aside in a safe place.</p>
                ''',
                'warning': 'The back cover has plastic tabs that can break if forced. If you feel resistance, check for missed screws.'
            },
            {
                'title': 'Remove the Heat Shield',
                'content': '''
                    <p>Removing the back cover will reveal the aluminium heat shield covering the motherboard. There are seven PH00 screws holding it and the sd card in place.
                    Firstly, remove the screw for the SD card and then pull directly up on it to disconnect it from the console. Then, remove the remaining six screws from the heat shield.
                    Finally, pull the heat sheild up and away from the switch.</p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step2.jpg" alt="Corner screw locations">
                    </div>
                ''',
                'warning': 'A small amount of resistance is to be expected when removing this, since there is viscous thermal paste in between the sheild and the copper heat sink underneath.'
            },
            {
                'title': 'Disconnect the Battery',
                'content': '''
                    <p>Using a spudger and not tweezers, lift the battery connector directly up and away from the console.</p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step7.png" alt="Corner screw locations">
                    </div>
                ''',
                'warning': 'Battery disconnection is a crucial safety step before proceeding with further disassembly. Do not disconnect any ribbon cables before completing this step.'
            },
            {
                'title': 'Remove the Copper Heatsink',
                'content': '''
                    <p>There are three PH00 screws that hold the copper heatsink in place, remove these and then either break the two bits of foam by the fan, or heat it up, and gently pry it up to prevent it from tearing. 
                    Then, remove the thermal paste from the heatsink and from the APU using a Q-Tip and Isopropyl alcohol.</p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step2.jpg" alt="Corner screw locations">
                    </div>
                '''
            },
            {
                'title': 'Removing the Game Card Slot',
                'content': '''
                    <p>The game card slot can be removed from the console. Firstly, take out the three PH00 silver screws holding the plastic tab for the audio jack and 
                    the one holding the game card slot in place. Make sure the ribbon cable for the touch screen is also removed. Pry up on the connector for the game card slot for the motherboard, and set it aside. 
                    </p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step2.jpg" alt="Corner screw locations">
                    </div>
                '''
            },
            {
                'title': 'Disconnecting Display and Other Cables',
                'content': '''
                    <p>You'll need to disconnect several ribbon cables: the large display cable near the top, 
                    touch screen cable beside it, volume and power button cables on the right, game card reader 
                    cable on the left, the Wi-Fi and Bluetooth antenna cables,both joycon rail ribbon cables and speaker cables on both sides. For each cable, locate the brown or black 
                    locking flip and use your spudger to gently lift it up 90 degrees. The cable should loosen 
                    automatically, allowing you to carefully pull it straight out. Make note of cable routing and 
                    orientation. The fan cable is right next to the power button cable, and the Wi-Fi cables are close to that, as shown in the photo. </p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step2.jpg" alt="Corner screw locations">
                    </div>
                ''',
                'warning': 'Ribbon cables are extremely fragile. Never force them or pull at an angle. If a cable feels stuck, double-check that the locking flip is fully released.'
            },
            {
                'title': 'Removing the Fan',
                'content': '''
                    <p>There are three black PH00 screws which hold the fan in place. Once these and the ribbon cable for it have been disconnected, the fan can be taken out of the console.
                    </p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step2.jpg" alt="Corner screw locations">
                    </div>
                '''
            },
            {
                'title': 'Removing the Motherboard',
                'content': '''
                    <p>There are four black PH00 cables which secure the motherboard into the console, and two silver ones by the charging port. Remove all of these from the console, and the motherboard can now be removed from the housing. 
                    </p>
                    <div class="guide-image">
                        <img src="/static/images/guides/switch/disassembly/step2.jpg" alt="Corner screw locations">
                    </div>
                '''
            },
            
        ],
        'troubleshooting': [
            {
                'problem': 'Screws strip easily',
                'solution': "Ensure you're using the correct size screwdriver and apply firm downward pressure while turning."
            },
            {
                'problem': "Screen doesn't work after reassembly",
                'solution': 'Double check that the display ribbon cable is fully inserted and the connector lock is engaged.'
            },
            {
                'problem': "Console won't power on after reassembly",
                'solution': 'Verify the battery connector is properly seated and all power button cables are connected.'
            },
            {
                'problem': 'Missing screws during reassembly',
                'solution': 'Different screw lengths are used in different locations. If unsure of screw placement, consult online repair guides for screw maps.'
            }
        ]
    }
    return render_template('guides/guide.html', **guide_content)




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

@nintendo_bp.route('/guides/switch-screen.html')
def switch_screen():
    content = {
        'console_tag': "nintendo",
        'console_name': "Nintendo Switch",
        'guide_title': "Touch Screen/LCD Screen Replacement Guide",
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