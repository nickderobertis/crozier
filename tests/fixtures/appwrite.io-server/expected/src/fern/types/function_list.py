

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function import Function


class FunctionList(UniversalBaseModel):
    """
    Functions List
    """

    functions: typing.List[Function] = pydantic.Field()
    """
    List of functions.
    """

    sum: int = pydantic.Field()
    """
    Total sum of items in the list.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
