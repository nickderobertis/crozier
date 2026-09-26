

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_channel_params_invalid_parameters_item import ErrorChannelParamsInvalidParametersItem


class ErrorChannelParams(UniversalBaseModel):
    """
    Invalid channel parameters
    """

    detail: str = pydantic.Field()
    """
    Additional information about the error
    """

    instance: str = pydantic.Field()
    """
    Internal Trace ID
    """

    invalid_parameters: typing.Optional[typing.List[ErrorChannelParamsInvalidParametersItem]] = None
    title: str = pydantic.Field()
    """
    Generic error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
