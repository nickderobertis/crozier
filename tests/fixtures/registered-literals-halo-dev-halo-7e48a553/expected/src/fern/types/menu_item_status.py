

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MenuItemStatus(UniversalBaseModel):
    """
    Resolved menu item values used for rendering.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(
            alias="displayName",
            description="Calculated display name after resolving targetRef, falling back to spec.displayName.",
        ),
    ] = None
    """
    Calculated display name after resolving targetRef, falling back to spec.displayName.
    """

    href: typing.Optional[str] = pydantic.Field(default=None)
    """
    Calculated href after resolving targetRef, falling back to spec.href.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
