

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EnhancedReportReportItemsItem(UniversalBaseModel):
    account_category: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="accountCategory"), pydantic.Field(alias="accountCategory")
    ] = None
    account_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountId"),
        pydantic.Field(alias="accountId", description="The unique account ID."),
    ] = None
    """
    The unique account ID.
    """

    account_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountName"),
        pydantic.Field(alias="accountName", description="Name of the account."),
    ] = None
    """
    Name of the account.
    """

    balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Balance of the account as reported on the profit and loss or Balance sheet.
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
