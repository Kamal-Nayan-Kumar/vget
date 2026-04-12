# User Testing Guide (macOS)

Download binary: https://github.com/Kamal-Nayan-Kumar/vget/releases/latest
Frontend dashboard: https://vget-teal.vercel.app/

```bash
chmod +x vget-macos-amd64
export VGET="./vget-macos-amd64"
export VGET_API_URL="https://vget-backend.onrender.com"

export PACKAGE_TO_INSTALL="data-security-quiz"
$VGET install "$PACKAGE_TO_INSTALL"

ls -la "./installed/$PACKAGE_TO_INSTALL/1.0.0"
cat "./installed/$PACKAGE_TO_INSTALL/1.0.0/index.js"
```
