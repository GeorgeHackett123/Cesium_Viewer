@echo off
setlocal enabledelayedexpansion

REM Output file
set "outfile=data\manifest.json"

REM Begin JSON array
echo [ > %outfile%

REM Loop through all .geojson files
set "first=true"
for %%f in (data\*.geojson) do (
    set "line=    \"%%~nxf\""
    if "!first!"=="true" (
        echo !line! >> %outfile%
        set "first=false"
    ) else (
        echo ,!line! >> %outfile%
    )
)

REM End JSON array
echo ] >> %outfile%

echo Manifest generated at %outfile%
pause
