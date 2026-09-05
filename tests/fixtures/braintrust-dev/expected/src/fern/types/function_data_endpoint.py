

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_data_endpoint_type import FunctionDataEndpointType


class FunctionDataEndpoint(UniversalBaseModel):
    """
    A remote eval to run
    """

    type: FunctionDataEndpointType
    endpoint: str
    eval_name: str
    parameters: typing.Dict[str, typing.Any]
    parameters_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version (transaction ID) of the parameters being used
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
