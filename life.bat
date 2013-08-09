:: Requires the path to python.exe to be added to environmental variable 'PATH'
@echo off
for %%X in (python.exe) do (set FOUND=%%~$PATH:X)
if defined FOUND (
	python src/main.py
) else (
	echo 'You don\'t have Python in your PATH... add it or run src/main.py manually...'
)