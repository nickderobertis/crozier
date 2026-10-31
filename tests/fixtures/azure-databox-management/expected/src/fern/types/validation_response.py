

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .validation_response_properties import ValidationResponseProperties


class ValidationResponse(UniversalBaseModel):
    """
    Response of pre job creation validations.
    """

    properties: typing.Optional[ValidationResponseProperties] = pydantic.Field(default=None)
    """
    Properties of pre job creation validation response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
