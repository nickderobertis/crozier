

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .api_reference import ApiReference
from .background_feature import BackgroundFeature


class Background(ApiReference):
    """
    `Background`
    """

    bonds: typing.Optional["Choice"] = None
    feature: typing.Optional[BackgroundFeature] = pydantic.Field(default=None)
    """
    Special feature granted to new characters of this background.
    """

    flaws: typing.Optional["Choice"] = None
    ideals: typing.Optional["Choice"] = None
    language_options: typing.Optional["Choice"] = None
    personality_traits: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Choice of personality traits for this background.
    """

    starting_equipment: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Starting equipment for all new characters of this background.
    """

    starting_equipment_options: typing.Optional["Choice"] = None
    starting_proficiencies: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Starting proficiencies for all new characters of this background.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .choice import Choice

update_forward_refs(Background)
