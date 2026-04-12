# Developer Testing Guide (macOS)

Download binary: https://github.com/Kamal-Nayan-Kumar/vget/releases/latest

```bash
chmod +x vget-macos-amd64
export VGET="./vget-macos-amd64"
export VGET_API_URL="https://vget-backend.onrender.com"

rm -rf ~/.vget
$VGET keygen

export DEV_USER="dev_$(date +%s)"
$VGET register --username "$DEV_USER" --password "secure123"
$VGET login --username "$DEV_USER" --password "secure123"
$VGET dev-register --username "$DEV_USER"

python3 vget-assistant/test_assistant.py

$VGET publish --path vget-assistant --version 1.0.0
```
