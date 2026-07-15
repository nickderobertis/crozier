

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference
from .resource_description import ResourceDescription


class AbilityScore(ApiReference, ResourceDescription):
    """
    `AbilityScore`
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name of the ability score.
    """

    skills: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of skills that use this ability score.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
