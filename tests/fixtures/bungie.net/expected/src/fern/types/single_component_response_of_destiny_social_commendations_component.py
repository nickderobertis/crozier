

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_components_social_destiny_social_commendations_component import (
    DestinyComponentsSocialDestinySocialCommendationsComponent,
)


class SingleComponentResponseOfDestinySocialCommendationsComponent(UniversalBaseModel):
    data: typing.Optional[DestinyComponentsSocialDestinySocialCommendationsComponent] = None
    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this component is disabled.
    """

    privacy: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
