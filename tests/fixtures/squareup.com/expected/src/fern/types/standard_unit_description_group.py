

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .standard_unit_description import StandardUnitDescription


class StandardUnitDescriptionGroup(UniversalBaseModel):
    """
    Group of standard measurement units.
    """

    language_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    IETF language tag.
    """

    standard_unit_descriptions: typing.Optional[typing.List[StandardUnitDescription]] = pydantic.Field(default=None)
    """
    List of standard (non-custom) measurement units in this description group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
