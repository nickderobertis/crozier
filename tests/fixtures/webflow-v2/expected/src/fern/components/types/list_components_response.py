

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_components_response_components_item import ListComponentsResponseComponentsItem
from .list_components_response_pagination import ListComponentsResponsePagination


class ListComponentsResponse(UniversalBaseModel):
    """
    List of Components on a site.
    """

    components: typing.Optional[typing.List[ListComponentsResponseComponentsItem]] = None
    pagination: typing.Optional[ListComponentsResponsePagination] = pydantic.Field(default=None)
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
