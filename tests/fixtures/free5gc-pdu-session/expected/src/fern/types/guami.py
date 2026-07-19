

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .plmn_id import PlmnId


class Guami(UniversalBaseModel):
    plmn_id: typing_extensions.Annotated[PlmnId, FieldMetadata(alias="plmnId"), pydantic.Field(alias="plmnId")]
    amf_id: typing_extensions.Annotated[str, FieldMetadata(alias="amfId"), pydantic.Field(alias="amfId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
