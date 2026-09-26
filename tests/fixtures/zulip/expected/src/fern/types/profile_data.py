

import typing

from .profile_data_value import ProfileDataValue

ProfileData = typing.Dict[str, ProfileDataValue]
"""
Only present if `is_bot` is false; bots can't have custom profile fields.

A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a single `value` key; for those custom profile fields
supporting Markdown, a `rendered_value` key will also be present.
"""
