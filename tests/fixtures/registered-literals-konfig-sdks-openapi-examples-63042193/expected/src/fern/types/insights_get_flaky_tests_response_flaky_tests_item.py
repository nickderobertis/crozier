

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .insights_get_flaky_tests_response_flaky_tests_item_job_number import (
    InsightsGetFlakyTestsResponseFlakyTestsItemJobNumber,
)
from .insights_get_flaky_tests_response_flaky_tests_item_pipeline_number import (
    InsightsGetFlakyTestsResponseFlakyTestsItemPipelineNumber,
)
from .insights_get_flaky_tests_response_flaky_tests_item_time_wasted import (
    InsightsGetFlakyTestsResponseFlakyTestsItemTimeWasted,
)


class InsightsGetFlakyTestsResponseFlakyTestsItem(UniversalBaseModel):
    time_wasted: typing_extensions.Annotated[
        typing.Optional[InsightsGetFlakyTestsResponseFlakyTestsItemTimeWasted],
        FieldMetadata(alias="time-wasted"),
        pydantic.Field(alias="time-wasted"),
    ] = None
    workflow_created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflow-created-at"),
        pydantic.Field(alias="workflow-created-at", description="The date and time when workflow was created."),
    ]
    """
    The date and time when workflow was created.
    """

    workflow_id: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="workflow-id"), pydantic.Field(alias="workflow-id")
    ]
    classname: str = pydantic.Field()
    """
    The class the test belongs to.
    """

    pipeline_number: typing_extensions.Annotated[
        InsightsGetFlakyTestsResponseFlakyTestsItemPipelineNumber,
        FieldMetadata(alias="pipeline-number"),
        pydantic.Field(alias="pipeline-number", description="The number of the pipeline."),
    ]
    """
    The number of the pipeline.
    """

    workflow_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflow-name"),
        pydantic.Field(alias="workflow-name", description="The name of the workflow."),
    ]
    """
    The name of the workflow.
    """

    test_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="test-name"), pydantic.Field(alias="test-name", description="The name of the test.")
    ]
    """
    The name of the test.
    """

    job_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="job-name"), pydantic.Field(alias="job-name", description="The name of the job.")
    ]
    """
    The name of the job.
    """

    job_number: typing_extensions.Annotated[
        InsightsGetFlakyTestsResponseFlakyTestsItemJobNumber,
        FieldMetadata(alias="job-number"),
        pydantic.Field(alias="job-number", description="The number of the job."),
    ]
    """
    The number of the job.
    """

    times_flaked: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="times-flaked"),
        pydantic.Field(alias="times-flaked", description="The number of times the test flaked."),
    ]
    """
    The number of times the test flaked.
    """

    source: str = pydantic.Field()
    """
    The source of the test.
    """

    file: str = pydantic.Field()
    """
    The file the test belongs to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
