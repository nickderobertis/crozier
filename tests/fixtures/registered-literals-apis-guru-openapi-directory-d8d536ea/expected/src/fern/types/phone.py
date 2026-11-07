

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .phone_phone_type import PhonePhoneType


class Phone(UniversalBaseModel):
    """
    Phone object data schema.
    """

    first_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="Date at which this record is created in UniCourt."),
    ]
    """
    Date at which this record is created in UniCourt.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(alias="isVisible", description="Boolean indicating if the phone is visible or not."),
    ]
    """
    Boolean indicating if the phone is visible or not.
    """

    last_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="Date at which this record was updated in UniCourt."),
    ]
    """
    Date at which this record was updated in UniCourt.
    """

    object: str
    phone_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="phoneNumber"), pydantic.Field(alias="phoneNumber", description="Phone Number")
    ]
    """
    Phone Number
    """

    phone_type: typing_extensions.Annotated[
        PhonePhoneType,
        FieldMetadata(alias="phoneType"),
        pydantic.Field(alias="phoneType", description="Resolved phone type (ideally from master data)."),
    ]
    """
    Resolved phone type (ideally from master data).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
