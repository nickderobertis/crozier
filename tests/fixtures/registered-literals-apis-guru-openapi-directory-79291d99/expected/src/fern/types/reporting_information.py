

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReportingInformation(UniversalBaseModel):
    """
    Information about an report identifier and a report name.
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
