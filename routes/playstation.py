from flask import Blueprint, render_template

playstation_bp = Blueprint('playstation', __name__)

@playstation_bp.route('/guides/ps5-ssd.html')
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

@playstation_bp.route('/guides/ps5-fan.html')
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

@playstation_bp.route('/guides/ps4-hdmi.html')
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

@playstation_bp.route('/guides/ps4-hdd.html')
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