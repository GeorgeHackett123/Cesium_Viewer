@echo off
setlocal enabledelayedexpansion

set "data_dir=data"
set "output_file=%data_dir%\manifest_other.json"
set "exclude=camera_points_final.geojson"

> "%output_file%" echo [

set "first=1"
for %%f in (%data_dir%\*.geojson) do (
    set "filename=%%~nxf"
    if /i not "!filename!"=="%exclude%" (
        if !first! == 1 (
            >> "%output_file%" echo,
        )
        >> "%output_file%" echo   "!filename!"
        set first=0
    )
)

>> "%output_file%" echo ]

echo ✅ Pretty JSON manifest written to %output_file%
pause
