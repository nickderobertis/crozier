

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemSeventySixData(UniversalBaseModel):
    """
    A dictionary containing the updated properties of the navigation view.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user-facing name for custom navigation views. Omit this field for built-in views.
    """

    is_pinned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines whether the view is pinned (true) or hidden in the menu (false).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
