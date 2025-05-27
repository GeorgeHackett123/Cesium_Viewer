@echo off
setlocal enabledelayedexpansion

REM Output file
set "outfile=data\manifest.json"

REM Start JSON array
echo [ > %outfile%

REM Track whether this is the first item
set "first=true"

REM Loop through all GeoJSON files in the data folder
for %%f in (data\*.geojson) do (
    if "!first!"=="true" (
        echo     "%%~nxf" >> %outfile%
        set "first=false"
    ) else (
        echo ,   "%%~nxf" >> %outfile%
    )
)

REM Close JSON array
echo ] >> %outfile%

echo Manifest generated successfully at %outfile%
pause
