

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TypesObjectWithUnknownField(UniversalBaseModel):
    """
    Tests that unknown/any values containing backslashes in map keys
    are properly escaped in Go string literals.
    """

    unknown: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
