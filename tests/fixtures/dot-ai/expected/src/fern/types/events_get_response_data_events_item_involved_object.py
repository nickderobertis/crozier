

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventsGetResponseDataEventsItemInvolvedObject(UniversalBaseModel):
    """
    Object this event is about
    """

    kind: str = pydantic.Field()
    """
    Resource kind
    """

    name: str = pydantic.Field()
    """
    Resource name
    """

    namespace: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource namespace
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource UID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
