

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TestResultSummary(UniversalBaseModel):
    """
    Represents the summary result of a Service or API test run by Microcks.
    """

    id: str = pydantic.Field()
    """
    Unique identifier of TestResult
    """

    service_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceId"),
        pydantic.Field(alias="serviceId", description="Unique identifier of service tested"),
    ]
    """
    Unique identifier of service tested
    """

    success: bool = pydantic.Field()
    """
    Flag telling if test is a success
    """

    test_date: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="testDate"),
        pydantic.Field(alias="testDate", description="Timestamp of creation date of this service"),
    ]
    """
    Timestamp of creation date of this service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
