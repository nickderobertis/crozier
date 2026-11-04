

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SetnestedSchemaItem(UniversalBaseModel):
    string_prop: typing.Optional[str] = pydantic.Field(default=None)
    """
    String inside a set!
    """

    bool_prop: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Bool inside a set!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
