

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_id import FunctionId
from .function_provider_id import FunctionProviderId


class Function(UniversalBaseModel):
    """
    Description of the exact function
    """

    function: FunctionId
    func_provider: FunctionProviderId
    uri: str = pydantic.Field()
    """
    Location description of function resources
    """

    configs: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    Optional parameters of the function instance
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
