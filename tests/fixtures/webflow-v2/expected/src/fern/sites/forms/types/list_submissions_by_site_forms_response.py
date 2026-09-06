

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_submissions_by_site_forms_response_form_submissions_item import (
    ListSubmissionsBySiteFormsResponseFormSubmissionsItem,
)
from .list_submissions_by_site_forms_response_pagination import ListSubmissionsBySiteFormsResponsePagination


class ListSubmissionsBySiteFormsResponse(UniversalBaseModel):
    """
    A list of form submissions
    """

    form_submissions: typing_extensions.Annotated[
        typing.Optional[typing.List[ListSubmissionsBySiteFormsResponseFormSubmissionsItem]],
        FieldMetadata(alias="formSubmissions"),
        pydantic.Field(alias="formSubmissions"),
    ] = None
    pagination: typing.Optional[ListSubmissionsBySiteFormsResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
