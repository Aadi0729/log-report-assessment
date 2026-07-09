from pathlib import Path


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"

import json
from pathlib import Path


def load_report():
    with open("/app/report.json", "r") as f:
        return json.load(f)


def test_total_requests():
    """Verifies success criterion 1: total_requests."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Verifies success criterion 2: unique_ips."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Verifies success criterion 3: top_path."""
    report = load_report()
    assert report["top_path"] == "/index.html"


def test_output_file():
    """Verifies success criterion 4: report written to the required path."""
    assert Path("/app/report.json").exists()
def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"
