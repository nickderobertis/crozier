

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .condition import Condition
from .page_layout import PageLayout
from .theme_status_phase import ThemeStatusPhase


class ThemeStatus(UniversalBaseModel):
    """
    Observed theme lifecycle and installation state.
    """

    conditions: typing.Optional[typing.List[Condition]] = pydantic.Field(default=None)
    """
    Reconciliation conditions for the theme.
    """

    entry: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resolved Console/User Center UI JavaScript entry URL served from the theme root.
    """

    in_development: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="inDevelopment"),
        pydantic.Field(
            alias="inDevelopment", description="Whether the theme appears to be a local development workspace."
        ),
    ] = None
    """
    Whether the theme appears to be a local development workspace.
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Local filesystem location where the theme is loaded from.
    """

    page_layout: typing_extensions.Annotated[
        typing.Optional[PageLayout], FieldMetadata(alias="pageLayout"), pydantic.Field(alias="pageLayout")
    ] = None
    phase: typing.Optional[ThemeStatusPhase] = pydantic.Field(default=None)
    """
    Current theme lifecycle phase.
    """

    screenshot: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resolved preview screenshot URL served from the theme root.
    """

    stylesheet: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resolved Console/User Center UI stylesheet URL served from the theme root.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
