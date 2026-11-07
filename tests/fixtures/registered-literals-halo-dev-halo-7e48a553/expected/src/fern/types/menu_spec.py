

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MenuSpec(UniversalBaseModel):
    """
    Desired menu configuration.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name shown for the menu."),
    ]
    """
    Display name shown for the menu.
    """

    menu_items: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="menuItems"),
        pydantic.Field(
            alias="menuItems",
            description="Legacy ordered root MenuItem names. Menu hierarchy is now sourced from MenuItem.spec.menuName and MenuItem.spec.parent.",
        ),
    ] = None
    """
    Legacy ordered root MenuItem names. Menu hierarchy is now sourced from MenuItem.spec.menuName and MenuItem.spec.parent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
