

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_content_components_response_nodes_item import GetContentComponentsResponseNodesItem
from .get_content_components_response_pagination import GetContentComponentsResponsePagination


class GetContentComponentsResponse(UniversalBaseModel):
    """
    The Component DOM schema represents the content structure of a component. Similar to Page DOM, it captures various content nodes and their associated attributes, but specifically for a component's structure. Each node has a unique identifier and can contain text, images, select or text inputs, submit buttons, or nested component instances.
    """

    component_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="componentId"),
        pydantic.Field(alias="componentId", description="Component ID"),
    ] = None
    """
    Component ID
    """

    nodes: typing.Optional[typing.List[GetContentComponentsResponseNodesItem]] = None
    pagination: typing.Optional[GetContentComponentsResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
