

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ComplianceAggregateCount(UniversalBaseModel):
    """
    Model for compliance aggregate count
    """

    critical_severity_failed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="criticalSeverityFailed"),
        pydantic.Field(alias="criticalSeverityFailed", description="Number of critical-severity failures"),
    ] = None
    """
    Number of critical-severity failures
    """

    failed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Failed
    """

    high_severity_failed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="highSeverityFailed"),
        pydantic.Field(alias="highSeverityFailed", description="Number of high-severity failures"),
    ] = None
    """
    Number of high-severity failures
    """

    informational_severity_failed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="informationalSeverityFailed"),
        pydantic.Field(alias="informationalSeverityFailed", description="Number of informational-severity failures"),
    ] = None
    """
    Number of informational-severity failures
    """

    low_severity_failed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lowSeverityFailed"),
        pydantic.Field(alias="lowSeverityFailed", description="Number of low-severity failures"),
    ] = None
    """
    Number of low-severity failures
    """

    medium_severity_failed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="mediumSeverityFailed"),
        pydantic.Field(alias="mediumSeverityFailed", description="Number of medium-severity failures"),
    ] = None
    """
    Number of medium-severity failures
    """

    passed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Passed
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
