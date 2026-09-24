

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .serial_config_parity import SerialConfigParity


class SerialConfig(UniversalBaseModel):
    port: str = pydantic.Field()
    """
    The port name for the serial connection
    """

    baud_rate: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="baudRate"),
        pydantic.Field(alias="baudRate", description="The baud rate for the serial connection"),
    ]
    """
    The baud rate for the serial connection
    """

    data_bits: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="dataBits"),
        pydantic.Field(alias="dataBits", description="The data bits for the serial connection"),
    ]
    """
    The data bits for the serial connection
    """

    stop_bits: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="stopBits"),
        pydantic.Field(alias="stopBits", description="The stop bits for the serial connection"),
    ]
    """
    The stop bits for the serial connection
    """

    parity: SerialConfigParity = pydantic.Field()
    """
    The parity for the serial connection
    """

    read_timeout: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="readTimeout"),
        pydantic.Field(alias="readTimeout", description="The read timeout for the serial connection in seconds"),
    ]
    """
    The read timeout for the serial connection in seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
