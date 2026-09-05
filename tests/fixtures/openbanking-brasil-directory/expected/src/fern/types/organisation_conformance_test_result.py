

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganisationConformanceTestResult(UniversalBaseModel):
    """
    a JSON response with the result of the test
    """

    result: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean with the result of the execution of the Conformance Suite Test
    """

    test_plan_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="testPlanUrl"),
        pydantic.Field(alias="testPlanUrl", description="URL of the published test plan result"),
    ] = None
    """
    URL of the published test plan result
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
