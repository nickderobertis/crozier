

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_resource_linked_resources_item import ApiResourceLinkedResourcesItem
from .resource_status import ResourceStatus


class ApiResource(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the resource, typically a lowercased version of name.
    """

    linked_resources: typing.Optional[typing.List[ApiResourceLinkedResourcesItem]] = pydantic.Field(default=None)
    """
    List of linked resources.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the resource (plural)
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="schema")
    ] = pydantic.Field(default=None)
    """
    JSON Schema of the resource in our Unified API
    """

    status: typing.Optional[ResourceStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
