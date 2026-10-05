

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PagerDutyUser(UniversalBaseModel):
    """
    PagerDuty user representation.

    Immutable model representing a user from PagerDuty API.

    Attributes:
        username: PagerDuty username (computed from email)
    """

    username: str = pydantic.Field()
    """
    PagerDuty username (computed from email)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
