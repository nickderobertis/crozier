

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsPagedClientStatusMetadata(UniversalBaseModel):
    limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Limit"),
        pydantic.Field(alias="Limit", description="The number of entities this paged response is limited to."),
    ] = None
    """
    The number of entities this paged response is limited to.
    """

    offset: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Offset"),
        pydantic.Field(alias="Offset", description="The number of entities prior to this page of items."),
    ] = None
    """
    The number of entities prior to this page of items.
    """

    report_result_expected: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ReportResultExpected"),
        pydantic.Field(
            alias="ReportResultExpected", description="The label for data contained in ClientStatus.ReportResults"
        ),
    ]
    """
    The label for data contained in ClientStatus.ReportResults
    """

    report_result_label: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ReportResultLabel"),
        pydantic.Field(
            alias="ReportResultLabel", description="The label for data contained in ClientStatus.ReportResults"
        ),
    ]
    """
    The label for data contained in ClientStatus.ReportResults
    """

    report_value_label: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ReportValueLabel"),
        pydantic.Field(
            alias="ReportValueLabel", description="The label for data contained in ClientStatus.ReportValue"
        ),
    ]
    """
    The label for data contained in ClientStatus.ReportValue
    """

    total_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TotalCount"),
        pydantic.Field(alias="TotalCount", description="The total number of entities matching the request."),
    ] = None
    """
    The total number of entities matching the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
