

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency import Currency


class DataIntegrityDetails(UniversalBaseModel):
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The transaction value.
    """

    connection_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="connectionId"),
        pydantic.Field(
            alias="connectionId",
            description="ID GUID representing the connection of the accounting or banking platform.",
        ),
    ] = None
    """
    ID GUID representing the connection of the accounting or banking platform.
    """

    currency: typing.Optional[Currency] = pydantic.Field(default=None)
    """
    The currency of the transaction.
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    In Codat's data model, dates and times are represented using the <a class="external" href="https://en.wikipedia.org/wiki/ISO_8601" target="_blank">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:
    
    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```
    
    
    
    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:
    
    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`
    
    > Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The transaction description.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID GUID of the transaction.
    """

    matches: typing.Optional[typing.List[typing.Any]] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The data type of the record.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
