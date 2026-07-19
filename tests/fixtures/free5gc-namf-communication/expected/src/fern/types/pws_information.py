

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2info_content import N2InfoContent


class PwsInformation(UniversalBaseModel):
    message_identifier: typing_extensions.Annotated[
        int, FieldMetadata(alias="messageIdentifier"), pydantic.Field(alias="messageIdentifier")
    ]
    serial_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="serialNumber"), pydantic.Field(alias="serialNumber")
    ]
    pws_container: typing_extensions.Annotated[
        N2InfoContent, FieldMetadata(alias="pwsContainer"), pydantic.Field(alias="pwsContainer")
    ]
    send_ran_response: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="sendRanResponse"), pydantic.Field(alias="sendRanResponse")
    ] = None
    omc_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="omcId"), pydantic.Field(alias="omcId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
