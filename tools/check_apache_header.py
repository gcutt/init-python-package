#!/usr/bin/env python3
import sys
import pathlib
import json
import datetime

CONFIG_PATH = pathlib.Path(__file__).parent / "license_config.json"

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"organization": "Unknown Organization"}

def build_header(config):
    year = datetime.date.today().year
    org = config.get("organization", "Unknown Organization")
    copyright_line = f"Copyright {year} {org}"
    return f"""{copyright_line}
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""

def has_header(content: str) -> bool:
    return "Apache License, Version 2.0" in content and "limitations under the License" in content

def fix_file(path: pathlib.Path, header: str):
    content = path.read_text(encoding="utf-8")
    if not has_header(content):
        print(f"⚠️ Adding Apache 2.0 header to {path}")
        new_content = header.strip() + "\n\n" + content
        path.write_text(new_content, encoding="utf-8")

def main(files):
    config = load_config()
    header = build_header(config)
    for f in files:
        path = pathlib.Path(f)
        if path.exists():
            fix_file(path, header)

if __name__ == "__main__":
    main(sys.argv[1:])