

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_addons_folders_list_response_item_attributes_categories_item import (
    NodesAddonsFoldersListResponseItemAttributesCategoriesItem,
)


class NodesAddonsFoldersListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the addon entity.
    """

    categories: typing.Optional[typing.List[NodesAddonsFoldersListResponseItemAttributesCategoriesItem]] = (
        pydantic.Field(default=None)
    )
    """
    List of categories this addon belongs to.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the service provider.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the third-party service provider.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to the third-party service provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
