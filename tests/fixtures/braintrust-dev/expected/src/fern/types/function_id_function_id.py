

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FunctionIdFunctionId(UniversalBaseModel):
    """
    Function id
    """

    function_id: str = pydantic.Field()
    """
    The ID of the function
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
