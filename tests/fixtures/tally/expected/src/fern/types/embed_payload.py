

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .embed_payload_display import EmbedPayloadDisplay
from .embed_payload_height import EmbedPayloadHeight
from .embed_payload_type import EmbedPayloadType
from .embed_payload_width import EmbedPayloadWidth
from .embed_provider import EmbedProvider
from .is_hidden import IsHidden


class EmbedPayload(UniversalBaseModel):
    """
    Payload for EMBED block type. Used for embedding external content.
    """

    is_hidden: typing_extensions.Annotated[
        typing.Optional[IsHidden], FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")
    ] = None
    type: typing.Optional[EmbedPayloadType] = None
    provider: typing.Optional[EmbedProvider] = None
    title: typing.Optional[str] = None
    input_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputUrl"), pydantic.Field(alias="inputUrl")
    ] = None
    display: typing.Optional[EmbedPayloadDisplay] = None
    width: typing.Optional[EmbedPayloadWidth] = None
    height: typing.Optional[EmbedPayloadHeight] = None
    column_list_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnListUuid], FieldMetadata(alias="columnListUuid"), pydantic.Field(alias="columnListUuid")
    ] = None
    column_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnUuid], FieldMetadata(alias="columnUuid"), pydantic.Field(alias="columnUuid")
    ] = None
    column_ratio: typing_extensions.Annotated[
        typing.Optional[ColumnRatio], FieldMetadata(alias="columnRatio"), pydantic.Field(alias="columnRatio")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
