

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .key_amf_type import KeyAmfType


class KeyAmf(UniversalBaseModel):
    key_type: typing_extensions.Annotated[KeyAmfType, FieldMetadata(alias="keyType"), pydantic.Field(alias="keyType")]
    key_val: typing_extensions.Annotated[str, FieldMetadata(alias="keyVal"), pydantic.Field(alias="keyVal")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
