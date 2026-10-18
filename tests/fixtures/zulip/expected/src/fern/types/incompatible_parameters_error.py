

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IncompatibleParametersError(UniversalBaseModel):
    result: typing.Any
    msg: typing.Any
    code: typing.Any
    parameters: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string containing the parameters, separated by commas,
    that are incompatible.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
