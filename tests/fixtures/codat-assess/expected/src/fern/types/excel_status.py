

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExcelStatus(UniversalBaseModel):
    error_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorMessage"), pydantic.Field(alias="errorMessage")
    ] = None
    file_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="fileSize"), pydantic.Field(alias="fileSize")
    ] = None
    in_progress: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="inProgress"), pydantic.Field(alias="inProgress")
    ] = None
    last_generated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastGenerated"),
        pydantic.Field(
            alias="lastGenerated",
            description='In Codat\'s data model, dates and times are represented using the <a class="external" href="https://en.wikipedia.org/wiki/ISO_8601" target="_blank">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:\n\n```\n2020-10-08T22:40:50Z\n2021-01-01T00:00:00\n```\n\n\n\nWhen syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:\n\n- Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`\n- Unqualified local time: `2021-11-15T01:00:00`\n- UTC time offsets: `2021-11-15T01:00:00-05:00`\n\n> Time zones\n> \n> Not all dates from Codat will contain information about time zones.  \n> Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.',
        ),
    ] = None
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

    last_invocation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastInvocationId"), pydantic.Field(alias="lastInvocationId")
    ] = None
    queued: typing.Optional[str] = None
    report_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="reportType"), pydantic.Field(alias="reportType")
    ] = None
    success: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
