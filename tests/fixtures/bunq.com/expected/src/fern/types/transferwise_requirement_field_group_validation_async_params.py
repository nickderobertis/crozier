

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferwiseRequirementFieldGroupValidationAsyncParams(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The parameter key.
    """

    parameter_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The parameter label.
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Shows whether the parameter is required or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
