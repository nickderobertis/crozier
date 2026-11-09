

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tree_view_model_license_list_item_agents_item import TreeViewModelLicenseListItemAgentsItem


class TreeViewModelLicenseListItem(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the license.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the license.
    """

    agents: typing.Optional[typing.List[TreeViewModelLicenseListItemAgentsItem]] = pydantic.Field(default=None)
    """
    List of agents associated with the license.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
