

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Unit(UniversalBaseModel):
    """
    Returns information about a unit of measurement
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the unit
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name of the unit
    """

    short_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Abbreviation of the unit
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
