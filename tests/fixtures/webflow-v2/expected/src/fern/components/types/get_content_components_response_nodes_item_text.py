

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_content_components_response_nodes_item_text_text import GetContentComponentsResponseNodesItemTextText


class GetContentComponentsResponseNodesItemText(UniversalBaseModel):
    """
    Represents text content within the DOM. It contains both the raw text and its HTML representation. Additional attributes can be associated with the text for styling or other purposes.
    """

    id: str = pydantic.Field()
    """
    Node UUID
    """

    text: GetContentComponentsResponseNodesItemTextText = pydantic.Field()
    """
    The text content of the node
    """

    attributes: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The custom attributes of the node
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
