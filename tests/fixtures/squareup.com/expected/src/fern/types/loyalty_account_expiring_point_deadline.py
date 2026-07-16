

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyAccountExpiringPointDeadline(UniversalBaseModel):
    """
    Represents a set of points for a loyalty account that are scheduled to expire on a specific date.
    """

    expires_at: str = pydantic.Field()
    """
    The timestamp of when the points are scheduled to expire, in RFC 3339 format.
    """

    points: int = pydantic.Field()
    """
    The number of points scheduled to expire at the `expires_at` timestamp.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
