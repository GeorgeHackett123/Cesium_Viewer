import os
import json
from pathlib import Path

# --- USER CONFIG --- #
CAMERA_POINTS_GEOJSON = 'camera_points_final.geojson'   # Change if needed
IMAGE_FOLDER = 'images'                                 # Used for validation only
OVERLAY_PATTERN = 'layer_*.geojson'
CESIUM_ION_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3MWVkZWM4Yi1hYzM2LTRmZDItOGVmZi1hMDliYzZjODA2NWMiLCJpZCI6MzA0NTQyLCJpYXQiOjE3NDg2MDYwMTZ9.IkBgYtVs-cpJykU4FRRGoHFUTaZoRsxYxslpmBnPM4o'                # Put your Cesium Ion token here

# Add custom colors for overlays as desired (filename: Cesium.Color expression as string)
CUSTOM_COLORS = {
    "layer_0.geojson": "Cesium.Color.WHITE",
    "layer_C-TOPO-MINR.geojson": "Cesium.Color.fromBytes(76,0,0,255)",
    "layer_C-TOPO-MAJR.geojson": "Cesium.Color.fromBytes(255,0,0,255)",
    "layer_TALUDE.geojson": "Cesium.Color.fromBytes(204,178,102,140)",
    "layer_MATRÍCULA.geojson": "Cesium.Color.fromBytes(0,191,255,255)",
    "layer_TOP-VEGETACAO.geojson": "Cesium.Color.fromBytes(0,255,0,255)",
    "layer_TOPO-BORDO.geojson": "Cesium.Color.fromBytes(0,0,0,98)"
}

TEMPLATE_FILE = "index_template.html"
OUTPUT_FILE = "index.html"
# ------------------- #

def list_overlay_geojsons(pattern):
    return sorted([str(p) for p in Path('.').glob(pattern)])

def make_custom_color_map(color_dict):
    # Output as a JS object (not JSON) so values are not quoted
    items = [f'"{k}": {v}' for k, v in color_dict.items()]
    return '{\n  ' + ',\n  '.join(items) + '\n}'

def main():
    # Find overlays
    overlays = list_overlay_geojsons(OVERLAY_PATTERN)
    print("Found overlay GeoJSONs:", overlays)
    overlay_json = json.dumps(overlays, ensure_ascii=False, indent=2)

    # Prepare color map
    color_map_js = make_custom_color_map(CUSTOM_COLORS)

    # Read template
    with open(TEMPLATE_FILE, encoding="utf-8") as f:
        template = f.read()

    # Replace placeholders
    result = template
    result = result.replace('{{CAMERA_POINTS_GEOJSON}}', CAMERA_POINTS_GEOJSON)
    result = result.replace('{{OVERLAY_GEOJSON_LIST}}', overlay_json)
    result = result.replace('{{CUSTOM_COLOR_MAP}}', color_map_js)
    result = result.replace('{{ION_TOKEN}}', CESIUM_ION_TOKEN)

    # Write output
    with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
        f.write(result)
    print(f"Output written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
