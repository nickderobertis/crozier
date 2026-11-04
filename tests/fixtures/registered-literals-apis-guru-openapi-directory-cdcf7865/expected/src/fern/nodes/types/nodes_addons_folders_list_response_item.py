

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_addons_folders_list_response_item_attributes import NodesAddonsFoldersListResponseItemAttributes


class NodesAddonsFoldersListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[NodesAddonsFoldersListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the addon entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the addon entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the addon entity (`addons`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
