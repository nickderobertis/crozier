

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.question import Question
from .list_form_submissions_response_submissions_item import ListFormSubmissionsResponseSubmissionsItem
from .list_form_submissions_response_total_number_of_submissions_per_filter import (
    ListFormSubmissionsResponseTotalNumberOfSubmissionsPerFilter,
)


class ListFormSubmissionsResponse(UniversalBaseModel):
    page: typing.Optional[float] = pydantic.Field(default=None)
    """
    Current page number
    """

    limit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of submissions per page
    """

    has_more: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMore"),
        pydantic.Field(alias="hasMore", description="Whether there are more pages available"),
    ] = None
    """
    Whether there are more pages available
    """

    total_number_of_submissions_per_filter: typing_extensions.Annotated[
        typing.Optional[ListFormSubmissionsResponseTotalNumberOfSubmissionsPerFilter],
        FieldMetadata(alias="totalNumberOfSubmissionsPerFilter"),
        pydantic.Field(alias="totalNumberOfSubmissionsPerFilter"),
    ] = None
    questions: typing.Optional[typing.List[Question]] = pydantic.Field(default=None)
    """
    List of form questions
    """

    submissions: typing.Optional[typing.List[ListFormSubmissionsResponseSubmissionsItem]] = pydantic.Field(default=None)
    """
    List of form submissions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
