

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Metadata(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The constant that defines the data set.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    A variable which belongs to the data set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
