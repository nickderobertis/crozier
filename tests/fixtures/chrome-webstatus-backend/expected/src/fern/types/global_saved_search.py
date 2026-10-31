

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .saved_search import SavedSearch


class GlobalSavedSearch(SavedSearch):
    """
    A system global saved search with its UI display order.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique string identifier for the saved search.
    """

    display_order: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UI sorting order for displaying in the sidebar.
    """

    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
