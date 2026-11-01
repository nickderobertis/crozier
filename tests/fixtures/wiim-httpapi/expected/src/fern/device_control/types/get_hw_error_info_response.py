

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_hw_error_info_response_sound_card_hw_error import GetHwErrorInfoResponseSoundCardHwError


class GetHwErrorInfoResponse(UniversalBaseModel):
    eth_error: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ethError"),
        pydantic.Field(alias="ethError", description="Ethernet error code"),
    ] = None
    """
    Ethernet error code
    """

    mfi_chip_error: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="mfiChipError"),
        pydantic.Field(alias="mfiChipError", description="MFi chip error code"),
    ] = None
    """
    MFi chip error code
    """

    flash_space_error: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="flashSpaceError"),
        pydantic.Field(alias="flashSpaceError", description="Flash space error code"),
    ] = None
    """
    Flash space error code
    """

    bad_block_num: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="badBlockNum"),
        pydantic.Field(alias="badBlockNum", description="Number of bad blocks in flash memory"),
    ] = None
    """
    Number of bad blocks in flash memory
    """

    total_block_num: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalBlockNum"),
        pydantic.Field(alias="totalBlockNum", description="Total number of blocks in flash memory"),
    ] = None
    """
    Total number of blocks in flash memory
    """

    hdmi_error: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="hdmiError"),
        pydantic.Field(alias="hdmiError", description="HDMI error code"),
    ] = None
    """
    HDMI error code
    """

    temperature_sensor_error: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="temperatureSensorError"),
        pydantic.Field(alias="temperatureSensorError", description="Temperature sensor error code"),
    ] = None
    """
    Temperature sensor error code
    """

    led_error: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ledError"),
        pydantic.Field(alias="ledError", description="LED error code"),
    ] = None
    """
    LED error code
    """

    sound_card_hw_error: typing_extensions.Annotated[
        typing.Optional[GetHwErrorInfoResponseSoundCardHwError],
        FieldMetadata(alias="soundCardHwError"),
        pydantic.Field(
            alias="soundCardHwError", description="Sound card hardware error codes for different components"
        ),
    ] = None
    """
    Sound card hardware error codes for different components
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
