

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventStreamCommon(UniversalBaseModel):
    """
    Describes an event stream mechanism available in this service instance
    """

    name: str = pydantic.Field()
    """
    Name of this type of event stream mechanism. Must be unique. Any name defined in this specification is reserved
    """

    docs: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location (e.g. a URL) at which documentation for this event stream mechanism may be found
    """

    config: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Configuration options required to make use of this mechanism
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
