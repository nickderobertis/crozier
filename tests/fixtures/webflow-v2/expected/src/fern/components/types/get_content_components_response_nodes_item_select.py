

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_content_components_response_nodes_item_select_choices_item import (
    GetContentComponentsResponseNodesItemSelectChoicesItem,
)


class GetContentComponentsResponseNodesItemSelect(UniversalBaseModel):
    """
    Represents select elements within the DOM. It contains the list of choices in the select. Additional attributes can be associated with the text for styling or other purposes.
    """

    id: str = pydantic.Field()
    """
    Node UUID
    """

    choices: typing.List[GetContentComponentsResponseNodesItemSelectChoicesItem] = pydantic.Field()
    """
    The list of choices in this select node.
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
