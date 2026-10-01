# llmlint: ignore-file[new_code_lands_in_a_project] crozier uses Cargo and just rather than Nx; this test belongs to the existing pytest live-e2e suite run by test-live-e2e.
"""The live harness reads committed corpus inputs through its real staging CLI."""
import subprocess

import pytest

from conftest import FIXTURES, Fixture, _FIXTURES, _spec_path


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda fixture: fixture.name)
def test_live_source_is_committed(fixture, tmp_path):
    source = _spec_path(fixture, tmp_path)
    assert source.is_file()
    if fixture.spec_url is None:
        assert source == _FIXTURES / fixture.name / "openapi.yml"
    else:
        committed = _FIXTURES / "corpus-sources" / fixture.name / source.name
        assert source.read_bytes() == committed.read_bytes()


def test_missing_live_source_reports_recovery(tmp_path):
    fixture = Fixture(name="not-a-registered-source", spec_url="https://invalid.example/spec")
    with pytest.raises(subprocess.CalledProcessError) as failure:
        _spec_path(fixture, tmp_path)
    assert "just lint-corpus-sources" in failure.value.stderr
