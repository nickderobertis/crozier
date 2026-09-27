

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PresenceWeights(UniversalBaseModel):
    """
    The weight set the composite was computed under. When the sync dimension is dropped the other three renormalize over 0.90, so these fractions reflect the mix actually used rather than the nominal weights.
    """

    rating: float = pydantic.Field()
    """
    Weight applied to ratingScore.
    """

    sla: float = pydantic.Field()
    """
    Weight applied to slaScore.
    """

    coverage: float = pydantic.Field()
    """
    Weight applied to coverageScore.
    """

    sync: float = pydantic.Field()
    """
    Weight applied to syncScore (0 when the sync dimension was dropped).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
