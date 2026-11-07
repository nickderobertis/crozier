

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .span_preparation_status import SpanPreparationStatus


class SpanPreparation(UniversalBaseModel):
    id: typing.Optional[str] = None
    screen_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="screenId"), pydantic.Field(alias="screenId")
    ] = None
    source_asset_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sourceAssetId"), pydantic.Field(alias="sourceAssetId")
    ] = None
    source_variant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sourceVariantId"), pydantic.Field(alias="sourceVariantId")
    ] = None
    status: typing.Optional[SpanPreparationStatus] = None
    progress: typing.Optional[float] = None
    error_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorCode"), pydantic.Field(alias="errorCode")
    ] = None
    error_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorMessage"), pydantic.Field(alias="errorMessage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
