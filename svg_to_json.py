import xml.etree.ElementTree as ET
import json
import re

def extract_provinces(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    # SVG namespace
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    provinces = []
    
    # Find all path elements
    for i, path in enumerate(root.findall('.//svg:path', ns)):
        province_id = path.get('id', f'province_{i}')
        
        # Extract path data
        d = path.get('d', '')
        
        # Extract style/color if needed
        style = path.get('style', '')
        
        province = {
            'id': province_id,
            'name': province_id.replace('_', ' ').title(),
            'path_data': d,
            'style': style,
            'centroid': calculate_centroid(d)  # You'll need to implement this
        }
        provinces.append(province)
    
    return provinces

def calculate_centroid(path_data):
    # Simplified centroid calculation
    # For production, use proper SVG path parsing
    return {"x": 0, "y": 0}

# Convert and save
provinces = extract_provinces('your_map.svg')

output = {
    'metadata': {
        'type': 'map_provinces',
        'coordinate_system': 'SVG',
        'provinces_count': len(provinces)
    },
    'provinces': provinces
}

with open('provinces.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"Exported {len(provinces)} provinces to provinces.json")
