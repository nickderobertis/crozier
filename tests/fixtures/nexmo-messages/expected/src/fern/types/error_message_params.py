

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_message_params_invalid_parameters_item import ErrorMessageParamsInvalidParametersItem


class ErrorMessageParams(UniversalBaseModel):
    """
    Invalid message parameters
    """

    detail: str = pydantic.Field()
    """
    Additional information about the error
    """

    instance: str = pydantic.Field()
    """
    Internal Trace ID
    """

    invalid_parameters: typing.Optional[typing.List[ErrorMessageParamsInvalidParametersItem]] = None
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
