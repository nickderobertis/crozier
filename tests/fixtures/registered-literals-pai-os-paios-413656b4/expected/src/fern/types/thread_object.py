

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_object_object import ThreadObjectObject


class ThreadObject(UniversalBaseModel):
    """
    Represents a thread that contains [messages](/docs/api-reference/messages).
    """

    id: str = pydantic.Field()
    """
    The identifier, which can be referenced in API endpoints.
    """

    object: ThreadObjectObject = pydantic.Field()
    """
    The object type, which is always `thread`.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the thread was created.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
