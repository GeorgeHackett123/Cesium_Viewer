@echo off
setlocal enabledelayedexpansion

set "data_dir=data"
set "output_file=%data_dir%\manifest_other.json"
set "exclude=camera_points_final.geojson"

(
    echo [
    set "first=1"
    for %%f in (%data_dir%\*.geojson) do (
        set "filename=%%~nxf"
        if /i not "!filename!"=="%exclude%" (
            if !first! == 1 (
                set "first=0"
            ) else (
                echo,
            )
            <nul set /p="    "!filename!""
        )
    )
    echo
    echo ]
) > "%output_file%"

echo ✅ manifest_other.json successfully created at: %output_file%
pause
