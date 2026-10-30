

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bluetooth_device_list_list_item import BluetoothDeviceListListItem


class BluetoothDeviceList(UniversalBaseModel):
    num: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of devices found
    """

    scan_status: typing.Optional[int] = pydantic.Field(default=None)
    """
    BT scan step
    0: Not started
    1: Initializing
    2: ??? (never seen it)
    3: Scanning
    4: Finished scanning
    """

    list_: typing_extensions.Annotated[
        typing.Optional[typing.List[BluetoothDeviceListListItem]],
        FieldMetadata(alias="list"),
        pydantic.Field(alias="list", description="List of devices found"),
    ] = None
    """
    List of devices found
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
