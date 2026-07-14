

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AnchoreErrorCode(UniversalBaseModel):
    """
    A description of an anchore error code (name, description)
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the error code
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error code name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
