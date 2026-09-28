

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .presence_recommendation_area import PresenceRecommendationArea


class PresenceRecommendation(UniversalBaseModel):
    """
    The single next-action nudge — the weakest present sub-score area, a localized message key the client resolves, and the composite points recovering that area to 100 would add.
    """

    area: PresenceRecommendationArea = pydantic.Field()
    """
    The composite dimension this recommendation targets.
    """

    message: str = pydantic.Field()
    """
    i18n message key the client resolves to a localized fix suggestion.
    """

    potential_gain: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="potentialGain"),
        pydantic.Field(
            alias="potentialGain",
            description="Composite points recovering this area to 100 would add (round(weight_of_area * (100 - subScore))).",
        ),
    ]
    """
    Composite points recovering this area to 100 would add (round(weight_of_area * (100 - subScore))).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
