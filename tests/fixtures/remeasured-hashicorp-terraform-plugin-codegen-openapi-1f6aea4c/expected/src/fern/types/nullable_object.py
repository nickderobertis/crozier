

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NullableObject(UniversalBaseModel):
    string_prop: str = pydantic.Field()
    """
    String inside a map!
    """

    bool_prop: bool = pydantic.Field()
    """
    Bool inside a map!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
