"""The live harness reads committed corpus inputs through its real staging CLI."""

import json
import subprocess

import pytest

from conftest import FIXTURES, Fixture, _FIXTURES, _spec_path


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda fixture: fixture.name)
def test_live_source_is_committed(fixture, tmp_path):
    source = _spec_path(fixture, tmp_path)
    assert source.is_file()
    if not fixture.registered_source:
        assert source == _FIXTURES / fixture.name / "openapi.yml"
    else:
        committed = _FIXTURES / "corpus-sources" / fixture.name / source.name
        assert source.read_bytes() == committed.read_bytes()


def test_missing_live_source_reports_recovery(tmp_path):
    fixture = Fixture(name="not-a-registered-source", registered_source=True)
    with pytest.raises(subprocess.CalledProcessError) as failure:
        _spec_path(fixture, tmp_path)
    assert "just lint-corpus-sources" in failure.value.stderr


def test_the_project_inputs_name_exactly_the_driven_fixtures():
    """`project.json` lists each driven fixture's files as cache and affected inputs:
    a fixture added to FIXTURES without its inputs would never rerun this suite."""
    project = json.loads((_FIXTURES.parent / "live_e2e" / "project.json").read_text(encoding="utf-8"))
    named = {
        entry
        for entry in project["targets"]["test"]["inputs"]
        if isinstance(entry, str)
        and entry.startswith("{workspaceRoot}/tests/fixtures/")
        and entry != "{workspaceRoot}/tests/fixtures/*.*"
    }
    expected = {f"{{workspaceRoot}}/tests/fixtures/{fixture.name}/**/*" for fixture in FIXTURES}
    expected |= {
        f"{{workspaceRoot}}/tests/fixtures/corpus-sources/{fixture.name}/**/*"
        for fixture in FIXTURES
        if fixture.registered_source
    }
    assert named == expected
