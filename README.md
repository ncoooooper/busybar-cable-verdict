# Cable Verdict

Compare the negotiated Mac power adapter profile to your expected wattage and read battery charge.

On a Mac laptop, choose the expected adapter wattage in the configuration. The bridge reads AppleSmartBattery from I/O Registry and battery percent from pmset. Watts refer to the adapter profile reported by macOS, not the instantaneous battery charging current. A disconnected or unreported adapter displays --. Browse to the second page for the battery.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
