

import typing

CustomProfileFieldDataSchema = typing.Dict[str, typing.Any]
"""
Field types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in the `field_data` attribute.

For field type 3 (Dropdown), this attribute is a JSON object
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.

The interface for field type 7 is not yet stabilized.

See [profile field types](/help/custom-profile-fields#profile-field-types)
or the [`field_type` parameter](/api/create-custom-profile-field#parameter-field_type)
for what each field type number means.
"""
