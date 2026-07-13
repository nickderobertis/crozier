

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transferwise_requirement_field_group_validation_async_params import (
    TransferwiseRequirementFieldGroupValidationAsyncParams,
)


class TransferwiseRequirementFieldGroupValidationAsync(UniversalBaseModel):
    params: typing.Optional[TransferwiseRequirementFieldGroupValidationAsyncParams] = pydantic.Field(default=None)
    """
    The parameters to send when validating user input.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url to be used to validate user input.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
