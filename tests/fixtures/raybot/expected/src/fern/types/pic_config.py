

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .serial_config import SerialConfig


class PicConfig(UniversalBaseModel):
    serial: SerialConfig
    enable_ack: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="enableAck"),
        pydantic.Field(alias="enableAck", description="Whether to enable the command ACK"),
    ]
    """
    Whether to enable the command ACK
    """

    command_ack_timeout: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="commandAckTimeout"),
        pydantic.Field(alias="commandAckTimeout", description="The timeout for the command ACK in milliseconds"),
    ]
    """
    The timeout for the command ACK in milliseconds
    """

    reset_pin: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="resetPin"),
        pydantic.Field(alias="resetPin", description="The pin number for the reset pin"),
    ]
    """
    The pin number for the reset pin
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
