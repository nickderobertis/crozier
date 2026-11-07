

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bar_record_status import BarRecordStatus
from .bar_source_data import BarSourceData
from .contact import Contact


class BarRecord(UniversalBaseModel):
    """
    This contains the Attorney details that is obtained from the State Bar where the attorney is registered.
    """

    admitted_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="admittedDate"),
        pydantic.Field(
            alias="admittedDate",
            description="The admittedDate is the date when an attorney was admitted to the bar of a given state.",
        ),
    ] = None
    """
    The admittedDate is the date when an attorney was admitted to the bar of a given state.
    """

    bar_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="barNumber"), pydantic.Field(alias="barNumber")
    ] = None
    bar_source_data: typing_extensions.Annotated[
        BarSourceData, FieldMetadata(alias="barSourceData"), pydantic.Field(alias="barSourceData")
    ]
    bar_source_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="barSourceType"), pydantic.Field(alias="barSourceType")
    ]
    contact: Contact
    first_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="firstFetchDate"), pydantic.Field(alias="firstFetchDate")
    ]
    inactivation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="inactivationDate"), pydantic.Field(alias="inactivationDate")
    ] = None
    last_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastFetchDate"), pydantic.Field(alias="lastFetchDate")
    ]
    last_fetch_date_with_updates: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDateWithUpdates"),
        pydantic.Field(alias="lastFetchDateWithUpdates", description="Last Fetch Date of the Attorney Update."),
    ]
    """
    Last Fetch Date of the Attorney Update.
    """

    object: str
    state_code: typing_extensions.Annotated[str, FieldMetadata(alias="stateCode"), pydantic.Field(alias="stateCode")]
    status: BarRecordStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
