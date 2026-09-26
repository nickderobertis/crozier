

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseCustomProfileFieldTypesValue(UniversalBaseModel):
    """
    `{FIELD_TYPE}`: Dictionary which contains the details
    of the field type with the field type as the name of the
    property itself. The current supported field types are as follows:

    - `SHORT_TEXT`
    - `PARAGRAPH`
    - `DATE` for date-based fields.
    - `DROPDOWN` for a list of options.
    - `URL` for links.
    - `EXTERNAL_ACCOUNT` for external accounts.
    - `USER` for selecting a user for the field.
    - `PRONOUNS` for a short text field with convenient typeahead for one's preferred pronouns.

    **Changes**: `PRONOUNS` type added in Zulip 6.0 (feature level 151).
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the custom profile field type.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the custom profile field type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
