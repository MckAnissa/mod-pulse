<p align="center">
  <img src="assets/banner.png" alt="Mod Pulse banner" width="800">
</p>

# Mod Pulse 🎮  
*A lightweight mod manager and file watcher.*

![Python](https://img.shields.io/badge/python-3.12-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview
**Mod Pulse** is a minimal command-line tool that monitors a mods folder, detects file changes in real time, and lists active mods.  
It’s ideal for organizing or debugging game mod directories without needing a heavy GUI manager.

## Features
- 🕵️ Detects new, modified, or deleted mod files  
- 📁 Lists all mods by directory  
- 🔄 Live watch mode for continuous monitoring  
- ⚙️ Lightweight and runs entirely locally  
- 🔐 `.env` file support for safe config management  

## Quickstart

```powershell
git clone https://github.com/MckAnissa/mod-pulse.git
cd mod-pulse
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
