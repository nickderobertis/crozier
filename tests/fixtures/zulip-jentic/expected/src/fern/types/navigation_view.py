

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NavigationView(UniversalBaseModel):
    """
    Represents a user's personal configuration for a specific
    navigation view (displayed most visibly at the top of the web
    application's left sidebar).

    Navigation views can be either an override to the default
    behavior of a built-in view, or a custom view.

    **Changes**: New in Zulip 11.0 (feature level 390).
    """

    fragment: str = pydantic.Field()
    """
    A unique identifier for the view, used to determine navigation
    behavior when clicked.
    
    Clients should use this value to navigate to the corresponding URL hash.
    """

    is_pinned: bool = pydantic.Field()
    """
    Determines whether the view appears directly in the sidebar or
    is hidden in the "More Views" menu.
    
    - `true` - Pinned and visible in the sidebar.
    - `false` - Hidden and accessible via the "More Views" menu.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user-facing name for custom navigation views. Omit this
    field for built-in views.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
