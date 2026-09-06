

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateStaticContentRequestNodesItemPlaceholder(UniversalBaseModel):
    """
    Update placeholder text on a text input node
    """

    node_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId", description="Node UUID")
    ]
    """
    Node UUID
    """

    placeholder: str = pydantic.Field()
    """
    The placeholder text of the input node
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
