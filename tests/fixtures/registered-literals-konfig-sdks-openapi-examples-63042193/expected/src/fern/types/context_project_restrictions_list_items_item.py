

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_project_restrictions_list_items_item_restriction_type import (
    ContextProjectRestrictionsListItemsItemRestrictionType,
)


class ContextProjectRestrictionsListItemsItem(UniversalBaseModel):
    context_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the context
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the restriction
    """

    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated - For "project" restrictions read the project ID from
    "restriction_value" instead.
    
    UUID of the project used in a project restriction.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contains a human-readable reference for the restriction. For
    "project" restrictions this is the name of the project.
    
    May be null.
    """

    restriction_type: typing.Optional[ContextProjectRestrictionsListItemsItemRestrictionType] = pydantic.Field(
        default=None
    )
    """
    Type of the restriction
    """

    restriction_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Value used to evaluate the restriction
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
