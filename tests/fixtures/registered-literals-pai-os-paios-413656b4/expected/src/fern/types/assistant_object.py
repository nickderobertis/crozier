

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistant_object_object import AssistantObjectObject
from .assistant_object_tools_item import AssistantObjectToolsItem


class AssistantObject(UniversalBaseModel):
    """
    Represents an `assistant` that can call the model and use tools.
    """

    id: str = pydantic.Field()
    """
    The identifier, which can be referenced in API endpoints.
    """

    object: AssistantObjectObject = pydantic.Field()
    """
    The object type, which is always `assistant`.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the assistant was created.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the assistant. The maximum length is 256 characters.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the assistant. The maximum length is 512 characters.
    """

    model: str = pydantic.Field()
    """
    ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.
    """

    instructions: typing.Optional[str] = pydantic.Field(default=None)
    """
    The system instructions that the assistant uses. The maximum length is 256,000 characters.
    """

    tools: typing.List[AssistantObjectToolsItem] = pydantic.Field()
    """
    A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.
    """

    file_ids: typing.List[str] = pydantic.Field()
    """
    A list of [file](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.
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
