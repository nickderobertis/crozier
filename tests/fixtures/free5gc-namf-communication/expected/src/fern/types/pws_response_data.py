

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tai import Tai


class PwsResponseData(UniversalBaseModel):
    ngap_message_type: typing_extensions.Annotated[
        int, FieldMetadata(alias="ngapMessageType"), pydantic.Field(alias="ngapMessageType")
    ]
    serial_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="serialNumber"), pydantic.Field(alias="serialNumber")
    ]
    message_identifier: typing_extensions.Annotated[
        int, FieldMetadata(alias="messageIdentifier"), pydantic.Field(alias="messageIdentifier")
    ]
    unknown_tai_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Tai]], FieldMetadata(alias="unknownTaiList"), pydantic.Field(alias="unknownTaiList")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
