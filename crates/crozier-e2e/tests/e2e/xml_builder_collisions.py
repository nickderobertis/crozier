"""Drive the XML builder names crozier gives colliding children, through the SDK
`xml_builder_collisions.yml` generates (`sdk_env_xml_builder_name_collisions_resolve_through_the_sdk`).
"""

import pydantic

from dock.types.manifest import Manifest
from dock.types.stamp import Stamp

# A builder named after its tag takes the name of the text field, which moves
# to a trailing-underscore attribute; the constructor still takes `note`.

manifest = Manifest(note="hello")
assert manifest.note_ == "hello"
note = manifest.note(author="ann")
assert note.author == "ann"
# Two children sharing the tag `entry` fall back to their class names.
manifest.crate_entry(weight=3)
manifest.pallet_entry(height=4)
# A tag naming pydantic's `copy` gains `add_`, so pydantic's method still answers.
manifest.add_copy(page=7)
assert Manifest.copy is pydantic.BaseModel.copy
xml = manifest.to_xml(xml_declaration=False)
for fragment in ('<note author="ann"', '<entry weight="3"', '<entry height="4"', '<copy page="7"', "hello"):
    assert fragment in xml, (fragment, xml)
assert Manifest.from_xml(xml).to_xml(xml_declaration=False) == xml
# An inherited text field cannot move, so the builder for its tag yields.
stamp = Stamp(label="red")
label = stamp.add_label(ink="blue")
assert (stamp.label, label.ink) == ("red", "blue")
assert '<label ink="blue"' in stamp.to_xml(xml_declaration=False)
print("ok")
