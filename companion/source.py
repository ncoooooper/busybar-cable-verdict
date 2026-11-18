"""Read actual adapter wattage and the laptop battery from macOS system tools."""
import json,plistlib,re,subprocess
from serve import page
INTERVAL=12
def metrics():
    raw=subprocess.check_output(["ioreg","-a","-r","-c","AppleSmartBattery"],timeout=5)
    cells=plistlib.loads(raw)
    if not cells:raise ValueError("No battery registered")
    info=cells[0];adapter=info.get("AdapterDetails",{})
    watts=adapter.get("Watts")
    text=subprocess.check_output(["pmset","-g","batt"],text=True,timeout=4)
    level=re.search(r"(\d+)%",text)
    if not level:raise ValueError("No battery reading")
    return int(level[1]),bool(info.get("ExternalConnected",False)),float(watts) if isinstance(watts,(float,int)) else None
def snapshot(o,m):
    level,connected,watts=metrics();target=float(o.get("expected_watts",67))
    if target<=0:raise ValueError("Expected watts must be positive")
    verdict="Unplugged" if not connected else "Unknown" if watts is None else "Below target" if watts<target else "Adequate"
    return dict(state=verdict,key=str(connected)+str(watts),pages=[
      page("USB-C PROFILE",f"{watts:g}W" if connected and watts is not None else "--",verdict,f"Expected {target:g} W",fraction=watts/target if connected and watts is not None else None),
      page("MAC BATTERY",str(level)+"%","On AC power" if connected else "On battery","Profile is adapter rating",fraction=level/100)])
