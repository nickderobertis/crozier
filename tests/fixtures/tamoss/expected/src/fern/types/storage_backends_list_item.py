

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .storage_backend import StorageBackend
from .uuid_ import Uuid


class StorageBackendsListItem(StorageBackend):
    id: typing.Optional[Uuid] = pydantic.Field(default=None)
    """
    Storage backend identifier
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Freeform string label for a storage backend.
    """

    default_storage: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to `true`, this is the default storage backend. The default storage backend will be used if the client does not specify a storage backend id when requesting the allocation of storage. If this parameter is not set, assume `false`. Service instances may either set one storage backend as default, or none - indicating that clients must always specify a storage backend.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
