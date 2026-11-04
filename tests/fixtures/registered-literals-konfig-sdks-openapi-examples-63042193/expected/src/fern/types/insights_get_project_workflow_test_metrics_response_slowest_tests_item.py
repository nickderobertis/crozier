

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InsightsGetProjectWorkflowTestMetricsResponseSlowestTestsItem(UniversalBaseModel):
    p95duration: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="p95_duration"),
        pydantic.Field(
            alias="p95_duration", description="The 95th percentile duration, in seconds, among a group of test runs."
        ),
    ]
    """
    The 95th percentile duration, in seconds, among a group of test runs.
    """

    total_runs: int = pydantic.Field()
    """
    The total number of times the test was run.
    """

    classname: str = pydantic.Field()
    """
    The class the test belongs to.
    """

    failed_runs: int = pydantic.Field()
    """
    The number of times the test failed
    """

    flaky: bool = pydantic.Field()
    """
    Whether the test is flaky.
    """

    source: str = pydantic.Field()
    """
    The source of the test.
    """

    file: str = pydantic.Field()
    """
    The file the test belongs to.
    """

    job_name: str = pydantic.Field()
    """
    The name of the job.
    """

    test_name: str = pydantic.Field()
    """
    The name of the test.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
