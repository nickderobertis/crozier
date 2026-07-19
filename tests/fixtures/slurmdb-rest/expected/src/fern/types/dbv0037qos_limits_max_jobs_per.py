

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037QosLimitsMaxJobsPer(UniversalBaseModel):
    """
    Limits on jobs per settings
    """

    account: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max jobs per account
    """

    user: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max jobs per user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
