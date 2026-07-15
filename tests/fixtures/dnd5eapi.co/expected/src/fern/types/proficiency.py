

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference


class Proficiency(ApiReference):
    """
    `Proficiency`
    """

    classes: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Classes that start with this proficiency.
    """

    races: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Races that start with this proficiency.
    """

    reference: typing.Optional[ApiReference] = pydantic.Field(default=None)
    """
    `APIReference` to the full description of the related resource.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The general category of the proficiency.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
