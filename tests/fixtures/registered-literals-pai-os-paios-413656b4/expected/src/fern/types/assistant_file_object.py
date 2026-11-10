

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistant_file_object_object import AssistantFileObjectObject


class AssistantFileObject(UniversalBaseModel):
    """
    A list of [Files](/docs/api-reference/files) attached to an `assistant`.
    """

    id: str = pydantic.Field()
    """
    The identifier, which can be referenced in API endpoints.
    """

    object: AssistantFileObjectObject = pydantic.Field()
    """
    The object type, which is always `assistant.file`.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the assistant file was created.
    """

    assistant_id: str = pydantic.Field()
    """
    The assistant ID that the file is attached to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
