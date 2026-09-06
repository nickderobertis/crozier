

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_static_content_request_nodes_item_choices_choices_item import (
    UpdateStaticContentRequestNodesItemChoicesChoicesItem,
)


class UpdateStaticContentRequestNodesItemChoices(UniversalBaseModel):
    """
    Update choices on a select node
    """

    node_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId", description="Node UUID")
    ]
    """
    Node UUID
    """

    choices: typing.List[UpdateStaticContentRequestNodesItemChoicesChoicesItem] = pydantic.Field()
    """
    The list of choices to set on the select node.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
