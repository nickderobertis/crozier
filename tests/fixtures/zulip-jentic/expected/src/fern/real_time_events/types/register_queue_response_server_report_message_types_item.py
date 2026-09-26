

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseServerReportMessageTypesItem(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID for the report message type.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user-facing string for the report message type, to be
    displayed in the report message UI, in the user's language.
    Note that the actual report will use the name for this type
    in the organization's default language.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
