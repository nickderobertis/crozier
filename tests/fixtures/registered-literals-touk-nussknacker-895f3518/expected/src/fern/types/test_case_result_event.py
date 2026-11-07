

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .results_with_counts_dto import ResultsWithCountsDto


class TestCaseResultEvent_Completed(UniversalBaseModel):
    type: typing.Literal["Completed"] = "Completed"
    test_case_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCaseId"), pydantic.Field(alias="testCaseId")
    ]
    test_case_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCaseName"), pydantic.Field(alias="testCaseName")
    ]
    result: ResultsWithCountsDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TestCaseResultEvent_Error(UniversalBaseModel):
    type: typing.Literal["Error"] = "Error"
    test_case_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCaseId"), pydantic.Field(alias="testCaseId")
    ]
    test_case_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCaseName"), pydantic.Field(alias="testCaseName")
    ]
    error: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TestCaseResultEvent = typing_extensions.Annotated[
    typing.Union[TestCaseResultEvent_Completed, TestCaseResultEvent_Error], pydantic.Field(discriminator="type")
]
