#!/bin/bash
sudo mkdir /var/log/Systemd_AI
sudo mkdir /usr/share/Systemd_AI
sudo cp .env /usr/share/Systemd_AI
sudo cp systemd_analyzer.py /usr/share/Systemd_AI
sudo cp requirements.txt /usr/share/Systemd_AI
sudo mv systemd-ai.service /etc/systemd/system/
sudo mv systemd-ai.timer /etc/systemd/system/
sudo python3 -m venv /usr/share/Systemd_AI/python_env
sudo /usr/share/Systemd_AI/python_env/bin/pip3 install -r requirements.txt
sudo systemctl daemon-reload
sudo systemctl enable --now systemd-ai.service
sudo systemctl enable --now systemd-ai.timer