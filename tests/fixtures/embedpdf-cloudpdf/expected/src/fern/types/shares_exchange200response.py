

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SharesExchange200Response(UniversalBaseModel):
    token: str
    doc_id: typing_extensions.Annotated[str, FieldMetadata(alias="docId"), pydantic.Field(alias="docId")]
    layer_name: typing_extensions.Annotated[str, FieldMetadata(alias="layerName"), pydantic.Field(alias="layerName")]
    expires_at: typing_extensions.Annotated[float, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
