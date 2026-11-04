

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .menu_item_spec_route_ref import MenuItemSpecRouteRef
from .menu_item_spec_target import MenuItemSpecTarget
from .ref import Ref


class MenuItemSpec(UniversalBaseModel):
    """
    Desired menu item configuration.
    """

    children: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Legacy child MenuItem names. Menu hierarchy is now sourced from MenuItem.spec.menuName and MenuItem.spec.parent.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name shown for the menu item."),
    ] = None
    """
    Display name shown for the menu item.
    """

    href: typing.Optional[str] = pydantic.Field(default=None)
    """
    Direct URL used by the menu item.
    """

    menu_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="menuName"),
        pydantic.Field(
            alias="menuName",
            description="Owning Menu metadata.name. Optional for compatibility with legacy raw payloads.",
        ),
    ] = None
    """
    Owning Menu metadata.name. Optional for compatibility with legacy raw payloads.
    """

    parent: typing.Optional[str] = pydantic.Field(default=None)
    """
    Parent MenuItem metadata.name in the same menu. Root items leave this unset.
    """

    priority: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sorting priority. Higher values sort before lower values where priority ordering is applied.
    """

    route_ref: typing_extensions.Annotated[
        typing.Optional[MenuItemSpecRouteRef],
        FieldMetadata(alias="routeRef"),
        pydantic.Field(alias="routeRef", description="Built-in theme route resolved into status.href."),
    ] = None
    """
    Built-in theme route resolved into status.href.
    """

    target: typing.Optional[MenuItemSpecTarget] = pydantic.Field(default=None)
    """
    HTML anchor target used by the menu item.
    """

    target_ref: typing_extensions.Annotated[
        typing.Optional[Ref], FieldMetadata(alias="targetRef"), pydantic.Field(alias="targetRef")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
