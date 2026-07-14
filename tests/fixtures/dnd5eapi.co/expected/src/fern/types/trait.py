

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .api_reference import ApiReference
from .resource_description import ResourceDescription
from .trait_trait_specific import TraitTraitSpecific


class Trait(ApiReference, ResourceDescription):
    """
    `Trait`
    """

    language_options: typing.Optional["Choice"] = None
    proficiencies: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of `Proficiencies` this trait grants.
    """

    proficiency_choices: typing.Optional["Choice"] = None
    races: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of `Races` that have access to the trait.
    """

    subraces: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of `Subraces` that have access to the trait.
    """

    trait_specific: typing.Optional[TraitTraitSpecific] = pydantic.Field(default=None)
    """
    Information specific to this trait
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .choice import Choice

update_forward_refs(Trait)
