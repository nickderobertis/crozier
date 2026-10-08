# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo CLI driven by just, with no Nx workspace; this documentary evidence script belongs to the linked departure or refusal evaluation and is run explicitly against the committed certified output or an identified generated SDK.
"""Validate the certified constructor placeholder against its date schema."""
import datetime
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[2]
client = root / 'openapi-surface/handwritten/observatory-client-date/fern-expected/src/fern/client.py'
source = client.read_text(encoding='utf-8')
assert 'sampling_day: typing.Optional[dt.date] = None' in source
placeholder = re.search(r'sampling_day="(YOUR_[A-Z_]+)"', source).group(1)
try:
    datetime.date.fromisoformat(placeholder)
except ValueError:
    pass
else:
    raise AssertionError('invalid date placeholder accepted')
assert datetime.date.fromisoformat('2023-01-15') == datetime.date(2023, 1, 15)
print('certified placeholder fails date validation; replacement passes')
