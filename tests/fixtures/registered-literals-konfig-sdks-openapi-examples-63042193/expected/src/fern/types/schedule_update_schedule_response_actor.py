

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScheduleUpdateScheduleResponseActor(UniversalBaseModel):
    """
    The attribution actor who will run the scheduled pipeline.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the user.
    """

    login: str = pydantic.Field()
    """
    The login information for the user on the VCS.
    """

    name: str = pydantic.Field()
    """
    The name of the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
