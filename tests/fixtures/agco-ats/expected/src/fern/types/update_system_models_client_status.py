

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsClientStatus(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientID"),
        pydantic.Field(alias="ClientID", description="The Client ID"),
    ] = None
    """
    The Client ID
    """

    last_checkin: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastCheckin"),
        pydantic.Field(alias="LastCheckin", description="The time of the client's last check-in"),
    ] = None
    """
    The time of the client's last check-in
    """

    minutes_elapsed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MinutesElapsed"),
        pydantic.Field(
            alias="MinutesElapsed", description="The number of minutes that have passed since the last check-in"
        ),
    ] = None
    """
    The number of minutes that have passed since the last check-in
    """

    report_result: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReportResult"),
        pydantic.Field(
            alias="ReportResult", description="The result for the client included in the UpdateGroup's report"
        ),
    ] = None
    """
    The result for the client included in the UpdateGroup's report
    """

    report_result_is_valid: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="ReportResultIsValid"),
        pydantic.Field(
            alias="ReportResultIsValid",
            description="True if the result for the client matches what is expected for the UpdateGroup",
        ),
    ] = None
    """
    True if the result for the client matches what is expected for the UpdateGroup
    """

    report_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReportValue"),
        pydantic.Field(
            alias="ReportValue", description="The value for the client included in the UpdateGroup's report"
        ),
    ] = None
    """
    The value for the client included in the UpdateGroup's report
    """

    tag: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Tag"),
        pydantic.Field(alias="Tag", description="A descriptive name for the client"),
    ] = None
    """
    A descriptive name for the client
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
