

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_project_restrictions_list_items_item import ContextProjectRestrictionsListItemsItem


class ContextProjectRestrictionsList(UniversalBaseModel):
    items: typing.Optional[typing.List[ContextProjectRestrictionsListItemsItem]] = None
    next_page_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Token that can be used to retrieve next page of results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
