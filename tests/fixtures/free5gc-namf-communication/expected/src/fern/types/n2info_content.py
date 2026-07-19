

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ngap_ie_type import NgapIeType
from .ref_to_binary_data import RefToBinaryData


class N2InfoContent(UniversalBaseModel):
    ngap_message_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ngapMessageType"), pydantic.Field(alias="ngapMessageType")
    ] = None
    ngap_ie_type: typing_extensions.Annotated[
        NgapIeType, FieldMetadata(alias="ngapIeType"), pydantic.Field(alias="ngapIeType")
    ]
    ngap_data: typing_extensions.Annotated[
        RefToBinaryData, FieldMetadata(alias="ngapData"), pydantic.Field(alias="ngapData")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
