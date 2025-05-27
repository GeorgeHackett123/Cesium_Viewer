@echo off
setlocal enabledelayedexpansion

set "data_dir=data"
set "output_file=%data_dir%\manifest_other.json"
set "exclude=camera_points_final.geojson"

rem Build manifest in memory first
set "manifest="

for %%f in (%data_dir%\*.geojson) do (
    set "filename=%%~nxf"
    if /i not "!filename!"=="%exclude%" (
        if defined manifest (
            set "manifest=!manifest!,"
        )
        set "manifest=!manifest!\"!filename!\""
    )
)

rem Write to file
> "%output_file%" echo [
>> "%output_file%" echo !manifest!
>> "%output_file%" echo ]

echo ✅ Fixed manifest generated: %output_file%
pause
