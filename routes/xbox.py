from flask import Blueprint, render_template

xbox_bp = Blueprint('xbox', __name__)

@xbox_bp.route('/guides/series-fan.html')
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

@xbox_bp.route('/guides/series-ssd.html')
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

@xbox_bp.route('/guides/xbone-hdmi.html')
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

@xbox_bp.route('/guides/xbone-hdd.html')
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