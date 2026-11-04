

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .menu_item import MenuItem


class MenuItemTreeNode(UniversalBaseModel):
    """
    Console MenuItem tree node.
    """

    children: typing.List["MenuItemTreeNode"]
    menu_item: typing_extensions.Annotated[MenuItem, FieldMetadata(alias="menuItem"), pydantic.Field(alias="menuItem")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(MenuItemTreeNode)
