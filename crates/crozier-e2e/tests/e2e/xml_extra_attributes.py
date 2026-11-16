"""An XML model's extra keyword arguments through the generated SDK: a declared
attribute's wire name sets that attribute, naming it twice or by a case-only
variant is refused, and any other name stays an undeclared attribute."""

from archive.types.record import Record

by_wire_name = Record("Charter", schemaLocation="urn:archive")
assert by_wire_name.xsi_schema_location == "urn:archive", by_wire_name
assert 'schemaLocation="urn:archive"' in by_wire_name.to_xml(), by_wire_name.to_xml()

for keywords, phrase in (
    ({"xsi_schema_location": "urn:a", "schemaLocation": "urn:b"}, "got both 'schemaLocation'"),
    ({"SchemaLocation": "urn:a"}, "did you mean 'schemaLocation'?"),
    ({"Lang": "en"}, "did you mean 'lang'?"),
):
    try:
        Record("Charter", **keywords)
    except TypeError as error:
        assert phrase in str(error), (keywords, error)
    else:
        raise AssertionError(f"Record accepted {keywords}")

undeclared = Record("Charter", lang="en", shelf="B4")
assert undeclared.lang == "en", undeclared
assert 'shelf="B4"' in undeclared.to_xml(), undeclared.to_xml()
print("ok")
