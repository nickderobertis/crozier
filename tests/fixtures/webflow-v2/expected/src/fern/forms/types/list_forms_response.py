

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_forms_response_forms_item import ListFormsResponseFormsItem
from .list_forms_response_pagination import ListFormsResponsePagination


class ListFormsResponse(UniversalBaseModel):
    """
    A list of forms
    """

    forms: typing.List[ListFormsResponseFormsItem]
    pagination: ListFormsResponsePagination = pydantic.Field()
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
