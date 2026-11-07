

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobGetDetailsResponseMessagesItem(UniversalBaseModel):
    """
    Message from CircleCI execution platform.
    """

    type: str = pydantic.Field()
    """
    Message type.
    """

    message: str = pydantic.Field()
    """
    Information describing message.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Value describing the reason for message to be added to the job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
