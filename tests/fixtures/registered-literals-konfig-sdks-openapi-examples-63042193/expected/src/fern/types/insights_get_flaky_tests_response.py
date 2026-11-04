

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .insights_get_flaky_tests_response_flaky_tests_item import InsightsGetFlakyTestsResponseFlakyTestsItem


class InsightsGetFlakyTestsResponse(UniversalBaseModel):
    """
    Flaky tests response
    """

    flaky_tests: typing_extensions.Annotated[
        typing.List[InsightsGetFlakyTestsResponseFlakyTestsItem],
        FieldMetadata(alias="flaky-tests"),
        pydantic.Field(
            alias="flaky-tests",
            description="A list of all instances of flakes. Note that a test is no longer considered flaky after 2 weeks have passed without a flake. Each flake resets this timer.",
        ),
    ]
    """
    A list of all instances of flakes. Note that a test is no longer considered flaky after 2 weeks have passed without a flake. Each flake resets this timer.
    """

    total_flaky_tests: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="total-flaky-tests"),
        pydantic.Field(
            alias="total-flaky-tests",
            description="A count of unique tests that have failed. If your project has N tests that have flaked multiple times each, this will be equal to N.",
        ),
    ]
    """
    A count of unique tests that have failed. If your project has N tests that have flaked multiple times each, this will be equal to N.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
