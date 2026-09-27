

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CollapsibleGroup(UniversalBaseModel):
    """
    A widget that groups the other widgets. All widgets that are within the area spanned by the grouping widget are considered member widgets.
    """

    collapsed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The collapsed state of the widget on first page load.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
