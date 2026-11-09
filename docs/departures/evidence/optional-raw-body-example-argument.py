# llmlint: ignore-file[new_code_lands_in_a_project] documentary evidence kept beside the departure's note.
"""Show the certified empty upload call failing to bind, and the corrected call binding."""

import inspect
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[3]
expected = root / "tests/fixtures/registered-literals-tryagi-assemblyai-215ec23d/expected"
# The certified client is importable only once its tree is on sys.path above.
sys.path.insert(0, str(expected / "src"))

from fern.files.client import FilesClient  # noqa: E402

source = (expected / "src/fern/files/client.py").read_text(encoding="utf-8")
assert "client.files.upload()\n" in source, "the certified docstring no longer writes the empty call"

signature = inspect.signature(FilesClient.upload)
client = object.__new__(FilesClient)
try:
    signature.bind(client)
except TypeError as error:
    print(f"certified call client.files.upload(): {error}")
else:
    raise SystemExit("the certified empty call binds; the defect is gone")
signature.bind(client, request=b"string")
print('corrected call client.files.upload(request=b"string"): binds')
