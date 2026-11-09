

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreditFreddieMacReportingInformationVoa24(UniversalBaseModel):
    """
    Information about an report identifier and a report name.
    """

    report_date_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReportDateTime"),
        pydantic.Field(
            alias="ReportDateTime",
            description="Documentation not found in the MISMO model viewer and not provided by Freddie Mac.",
        ),
    ] = None
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    report_identifier_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReportIdentifierType"),
        pydantic.Field(
            alias="ReportIdentifierType",
            description='Documentation not found in the MISMO model viewer and not provided by Freddie Mac. The value can only be "ReportID"',
        ),
    ] = None
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac. The value can only be "ReportID"
    """

    reporting_information_identifier: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ReportingInformationIdentifier"),
        pydantic.Field(
            alias="ReportingInformationIdentifier",
            description="Documentation not found in the MISMO model viewer and not provided by Freddie Mac.",
        ),
    ]
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
