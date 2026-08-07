#!/usr/bin/env python3
from pathlib import Path

module = (Path(__file__).resolve().parents[1] / "modules/wloc.module").read_text()
expected = "hostname = %APPEND% gs-loc.apple.com, gs-loc-cn.apple.com"

assert module.count(expected) == 1, "approved hostname line is missing or duplicated"
assert "refs/heads/main/dist/" not in module, "runtime scripts must be commit-pinned"
assert module.count("169375c17ae4d6ef444f5ec910acf4be6750640c/dist/") == 2
print("distribution policy OK")
