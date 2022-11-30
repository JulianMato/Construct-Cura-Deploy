"""
Zachary Cook, Julian Mato-Hernandez

Common configuration for the deployment.
"""

# Known locations for the Cura installs.
KNOWN_CURA_LOCATIONS = ["C:/Program Files/"]

# Host for the server.
SERVER_HOST = "https://hack.rit.edu:7000"

# Modifications made to the printer profiles.
PRINTER_OVERRIDES = {
    "prusa_i3_mk3.def.json": {
        "adhesion_type": { "default_value": "brim" },
        "support_enable": { "default_value": True },
        "infill_sparse_density": { "default_value": 15 },
        "raft_margin": { "default_value": 5 },
    },
    "artillery_base.def.json": {
        "adhesion_type": { "default_value": "raft" },
        "support_enable": { "default_value": True },
        "infill_sparse_density": { "default_value": 15 },
        "raft_margin": { "default_value": 5 },
        "support_infill_rate": { "value": "0 if support_enable and support_structure == 'tree' else 15" },
        "support_use_towers": { "value": True },
        "support_wall_count": { "value": 0 },
        "support_brim_enable": { "value": False },
        "machine_start_gcode": { "default_value": "M511 P3ZDZV2FxW ; Unlock printer\n G28 ; home all axes\n M117 Purge extruder\n G92 E0 ; reset extruder\n G1 Z1.0 F3000 ; move z up little to prevent scratching of surface\n G1 X2 Y20 Z0.3 F5000.0 ; move to start-line position\n G1 X2 Y200.0 Z0.3 F1500.0 E15 ; draw 1st line\n G1 X2 Y200.0 Z0.4 F5000.0 ; move to side a little\n G1 X2 Y20 Z0.4 F1500.0 E30 ; draw 2nd line\n G92 E0 ; reset extruder\n G1 Z1.0 F3000 ; move z up little to prevent scratching of surface"},
        "machine_end_gcode": { "default_value": "G91; relative positioning\n G1 Z1.0 F3000 ; move z up little to prevent scratching of print\n G90; absolute positioning\n G1 X0 Y200 F1000 ; prepare for part removal\n M104 S0; turn off extruder\n M140 S0 ; turn off bed\n G1 X0 Y300 F1000 ; prepare for part removal\n M84 ; disable motors\n M106 S0 ; turn off fan\n M510 ; lock printer" },
    },
}

# Modifications made to the material profiles.
MATERIAL_OVERRIDES = {
    "generic_pla_175.xml.fdm_material": {
        "print temperature": 210,
    }
}