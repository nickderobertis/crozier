

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .page_layout_state import PageLayoutState


class PageLayout(UniversalBaseModel):
    """
    Page layout contract compatibility details.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable diagnostic message.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stable diagnostic reason.
    """

    state: typing.Optional[PageLayoutState] = pydantic.Field(default=None)
    """
    Compatibility state of the page layout contract.
    """

    template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contract template path relative to the theme root.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
