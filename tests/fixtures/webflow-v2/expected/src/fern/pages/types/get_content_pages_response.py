

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_content_pages_response_nodes_item import GetContentPagesResponseNodesItem
from .get_content_pages_response_pagination import GetContentPagesResponsePagination


class GetContentPagesResponse(UniversalBaseModel):
    """
    The DOM (Document Object Model) schema represents the content structure of a web page or component. It captures various content nodes along with their associated attributes. Each node has a unique identifier and can be of different types like text, image or component-instance. The schema also provides pagination details for scenarios where the content nodes are too many to be fetched in a single request.
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pageId"), pydantic.Field(alias="pageId", description="Page ID")
    ] = None
    """
    Page ID
    """

    branch_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="branchId"),
        pydantic.Field(
            alias="branchId",
            description="The unique identifier of a [specific page branch.](https://help.webflow.com/hc/en-us/articles/33961355506195-Page-branching)",
        ),
    ] = None
    """
    The unique identifier of a [specific page branch.](https://help.webflow.com/hc/en-us/articles/33961355506195-Page-branching)
    """

    nodes: typing.Optional[typing.List[GetContentPagesResponseNodesItem]] = None
    pagination: typing.Optional[GetContentPagesResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the page dom was most recently updated"),
    ] = None
    """
    The date the page dom was most recently updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
