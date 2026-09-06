

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventActionUserInactivity(UniversalBaseModel):
    disable_threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    Inactivity threshold, in days, before disabling the account
    """

    delete_threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    Inactivity threshold, in days, before deleting the account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
