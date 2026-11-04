

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .triple_nested_map_schema import TripleNestedMapSchema


class EdgecaseProvider(UniversalBaseModel):
    """
    This is the provider schema
    """

    string_prop: str = pydantic.Field()
    """
    String for the provider
    """

    bool_prop: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Bool for the provider
    """

    triple_nested_map: TripleNestedMapSchema

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
