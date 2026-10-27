

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class SendChannelMessageRequestHostedContentsItem(UniversalBaseModel):
    microsoft_graph_temporary_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="@microsoft.graph.temporaryId"),
        pydantic.Field(alias="@microsoft.graph.temporaryId"),
    ] = None
    content_bytes: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentBytes"), pydantic.Field(alias="contentBytes")
    ] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
