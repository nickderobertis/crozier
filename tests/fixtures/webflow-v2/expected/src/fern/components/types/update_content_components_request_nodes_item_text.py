

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateContentComponentsRequestNodesItemText(UniversalBaseModel):
    """
    Update a text node
    """

    node_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId", description="Node UUID")
    ]
    """
    Node UUID
    """

    text: str = pydantic.Field()
    """
    HTML content of the node, including the HTML tag. The HTML tags must be the same as what's returned from the Get Content endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
