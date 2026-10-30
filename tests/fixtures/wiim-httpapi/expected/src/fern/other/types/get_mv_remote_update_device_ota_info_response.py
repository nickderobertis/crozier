

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_mv_remote_update_device_ota_info_response_img_list_item import (
    GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem,
)


class GetMvRemoteUpdateDeviceOtaInfoResponse(UniversalBaseModel):
    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device language
    """

    project_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="projectId"),
        pydantic.Field(alias="projectId", description="Project identifier"),
    ] = None
    """
    Project identifier
    """

    fw_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fwVersion"),
        pydantic.Field(alias="fwVersion", description="Firmware version"),
    ] = None
    """
    Firmware version
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version
    """

    mac_addr: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="macAddr"), pydantic.Field(alias="macAddr", description="MAC address")
    ] = None
    """
    MAC address
    """

    serial_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serialNumber"),
        pydantic.Field(alias="serialNumber", description="Serial number"),
    ] = None
    """
    Serial number
    """

    device_uid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deviceUid"),
        pydantic.Field(alias="deviceUid", description="Device UID"),
    ] = None
    """
    Device UID
    """

    img_list: typing_extensions.Annotated[
        typing.Optional[typing.List[GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem]],
        FieldMetadata(alias="imgList"),
        pydantic.Field(alias="imgList", description="List of images"),
    ] = None
    """
    List of images
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
