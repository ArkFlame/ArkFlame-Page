@echo off
cd /d "%~dp0"
py preview-local.py || python preview-local.py
pause
