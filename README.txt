Cesium + Marzipano Automated 360 Viewer
=======================================

This project automates the creation of a CesiumJS + Marzipano 360° imagery viewer for new camera points, overlays, and images.

-------------------------------------------------------------------------------

FOLDER STRUCTURE

your-project-folder/
├── build_cesium_index.py        # Automation script (run this)
├── index_template.html          # HTML template with placeholders
├── camera_points_final.geojson  # Main camera points GeoJSON (can be renamed)
├── layer_0.geojson              # Overlay GeoJSON(s) (auto-detected)
├── layer_C-TOPO-MAJR.geojson
├── ... more layer_*.geojson ...
├── images/                      # Folder with all 360 images
│    ├── IMG_0001.JPG
│    ├── IMG_0002.JPG
│    └── ...
└── index.html                   # Generated output (viewer)

-------------------------------------------------------------------------------

HOW TO USE

1. Prepare your data:
   - Place your main camera points GeoJSON in the folder (default: camera_points_final.geojson).
     - The filename is set in build_cesium_index.py (CAMERA_POINTS_GEOJSON).
     - Each feature must have a #Label property matching its image filename, and a Yaw_est value.
   - Put all overlay/annotation GeoJSON files (matching layer_*.geojson) in the folder.
   - Place all 360 images in the images/ folder.
     - Filenames must match the #Label value in the camera points GeoJSON.

2. Update Config (if needed):
   - If your camera points GeoJSON is named differently, update CAMERA_POINTS_GEOJSON in build_cesium_index.py.
   - Add/change overlay filenames or custom overlay colors in the script’s CUSTOM_COLORS dictionary.
   - Paste your Cesium Ion token in the CESIUM_ION_TOKEN variable.

3. Generate your viewer:
   - From a terminal/command prompt in the folder, run:
     python build_cesium_index.py
   - This will:
     - Scan your overlay GeoJSON files,
     - Fill in the template,
     - Output a complete index.html viewer.

4. View your site:
   - Open index.html in your browser (or upload all contents to your web server/GitHub Pages).

-------------------------------------------------------------------------------

UPDATING WITH NEW DATA

1. Replace or add your new camera_points_final.geojson and/or overlays.
2. Place new 360 images in the images/ folder (ensure filenames match).
3. Re-run:
   python build_cesium_index.py
4. Upload or deploy as needed.

-------------------------------------------------------------------------------

TROUBLESHOOTING

- Missing images:
    Make sure every #Label in the camera points GeoJSON has a matching image in the images/ folder.

- New overlay files:
    Overlay GeoJSONs matching layer_*.geojson are detected automatically. Add new ones as needed.

- Custom colors:
    Update the CUSTOM_COLORS dictionary in the script if you want new overlays to have custom map colors.

-------------------------------------------------------------------------------

ADVANCED

- You can change the overlay GeoJSON file pattern or add more config logic in build_cesium_index.py.
- For large datasets, consider automating the creation of camera points and images with your own scripts.

-------------------------------------------------------------------------------

REQUIREMENTS

- Python 3.x
- Cesium Ion account/token (https://cesium.com/ion/)

-------------------------------------------------------------------------------

CONTACT

For improvements or support, ask your project admin or OpenAI ChatGPT for script tweaks!
