

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .menu_item_spec import MenuItemSpec
from .menu_item_status import MenuItemStatus
from .metadata import Metadata


class MenuItem(UniversalBaseModel):
    """
    Menu item extension that describes a navigable item and its resolved rendering state.
    """

    api_version: typing_extensions.Annotated[str, FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion")]
    kind: str
    metadata: Metadata
    spec: MenuItemSpec
    status: typing.Optional[MenuItemStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
