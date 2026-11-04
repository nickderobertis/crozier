

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DetailsErrorFailedConstraintsItem(UniversalBaseModel):
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the violated constraint.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the field that violated the constraint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
