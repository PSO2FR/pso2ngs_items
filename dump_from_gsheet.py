from genericpath import exists
import os
import logging

import requests

SHEETS=[
    {"key": "1wMXrCwKeqUGdrpuIFG8Omu_v4Gfs2rjOJfx4rfYrILY", "gid": "0", "output": "weapons/swords.csv"},

    {"key": "1NLm8hgg09ChiBcbQedyt0dniuJxaGRo-C_Ca6GWfDiQ", "gid": "0", "output": "photon_arts/swords.csv"},

    {"key": "17w5v1UHKj3eFPcziqAR111AIBFVD3cY3l7Wz3wBpy_4", "gid": "0", "output": "techniques/fire.csv"},
    {"key": "17w5v1UHKj3eFPcziqAR111AIBFVD3cY3l7Wz3wBpy_4", "gid": "0", "output": "techniques/ice.csv"},
    {"key": "17w5v1UHKj3eFPcziqAR111AIBFVD3cY3l7Wz3wBpy_4", "gid": "0", "output": "techniques/lightning.csv"},
    {"key": "17w5v1UHKj3eFPcziqAR111AIBFVD3cY3l7Wz3wBpy_4", "gid": "0", "output": "techniques/wind.csv"},
    {"key": "17w5v1UHKj3eFPcziqAR111AIBFVD3cY3l7Wz3wBpy_4", "gid": "0", "output": "techniques/light.csv"},
    {"key": "17w5v1UHKj3eFPcziqAR111AIBFVD3cY3l7Wz3wBpy_4", "gid": "0", "output": "techniques/dark.csv"},
]

def download_sheet(key, gid, output, encoding="utf-8"):
    r = requests.get('https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:csv&gid=%s' % (key, gid))

    if r.status_code != 200:
        logging.error("Can't query for: %s (%s)" % (key, gid))
        return

    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output), exist_ok=True)

    with open(output, "w", encoding=encoding) as f:
        f.write(r.text)

if __name__ == "__main__":
    for sheet in SHEETS:
        logging.info("Downloading %s (%s) to %s" % (sheet["key"], sheet["gid"], sheet["output"]))
        download_sheet(sheet["key"], sheet["gid"], sheet["output"])