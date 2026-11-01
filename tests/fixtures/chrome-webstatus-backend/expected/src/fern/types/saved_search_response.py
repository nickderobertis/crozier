

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .generic_updatable_unique_model import GenericUpdatableUniqueModel
from .saved_search import SavedSearch
from .user_saved_search_bookmark import UserSavedSearchBookmark
from .user_saved_search_permissions import UserSavedSearchPermissions


class SavedSearchResponse(GenericUpdatableUniqueModel, SavedSearch):
    permissions: typing.Optional[UserSavedSearchPermissions] = None
    bookmark_status: typing.Optional[UserSavedSearchBookmark] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
