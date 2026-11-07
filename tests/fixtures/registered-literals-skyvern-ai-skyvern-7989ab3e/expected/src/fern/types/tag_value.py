

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TagValue(UniversalBaseModel):
    """
    Tag-value color registry entry: the palette color assigned to a grouped
    (key, value) pair.
    """

    key: str
    value: str
    color: str
    workflow_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of non-deleted workflows currently carrying this (key, value) label.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
