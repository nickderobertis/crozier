

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FragmentUsageData(UniversalBaseModel):
    fragment_node_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="fragmentNodeId"), pydantic.Field(alias="fragmentNodeId")
    ]
    fragment_node_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="fragmentNodeName"), pydantic.Field(alias="fragmentNodeName")
    ]
    node_id: typing_extensions.Annotated[str, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId")]
    node_name: typing_extensions.Annotated[str, FieldMetadata(alias="nodeName"), pydantic.Field(alias="nodeName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
