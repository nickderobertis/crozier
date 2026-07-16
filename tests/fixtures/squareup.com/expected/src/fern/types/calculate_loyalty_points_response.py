

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error


class CalculateLoyaltyPointsResponse(UniversalBaseModel):
    """
    A response that includes the points that the buyer can earn from
    a specified purchase.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    points: typing.Optional[int] = pydantic.Field(default=None)
    """
    The points that the buyer can earn from a specified purchase.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
