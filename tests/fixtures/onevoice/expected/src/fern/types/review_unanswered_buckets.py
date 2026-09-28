

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReviewUnansweredBuckets(UniversalBaseModel):
    """
    Unanswered reviews partitioned by age (created_at -> now).
    """

    lt24h: int = pydantic.Field()
    """
    Unanswered under 24 hours old.
    """

    h24to72: int = pydantic.Field()
    """
    Unanswered between 24 and 72 hours old.
    """

    gt72h: int = pydantic.Field()
    """
    Unanswered over 72 hours old.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
