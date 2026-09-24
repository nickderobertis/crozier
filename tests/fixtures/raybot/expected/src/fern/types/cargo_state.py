

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CargoState(UniversalBaseModel):
    is_open: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isOpen"), pydantic.Field(alias="isOpen", description="Whether the cargo is open")
    ]
    """
    Whether the cargo is open
    """

    qr_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="qrCode"),
        pydantic.Field(alias="qrCode", description="The QR code read from the cargo QR scanner"),
    ]
    """
    The QR code read from the cargo QR scanner
    """

    bottom_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="bottomDistance"),
        pydantic.Field(alias="bottomDistance", description="The bottom distance of the cargo"),
    ]
    """
    The bottom distance of the cargo
    """

    has_item: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasItem"),
        pydantic.Field(alias="hasItem", description="Whether the cargo has an item"),
    ]
    """
    Whether the cargo has an item
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the cargo"),
    ]
    """
    The updated at time of the cargo
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
