

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1OrderHistoryEntry(UniversalBaseModel):
    """
    V1OrderHistoryEntry
    """

    action: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of action performed on the order.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the action was performed, in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
