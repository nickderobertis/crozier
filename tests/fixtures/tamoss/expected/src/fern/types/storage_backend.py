

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .storage_backend_store_type import StorageBackendStoreType


class StorageBackend(UniversalBaseModel):
    """
    Provides technical, and logic metadata about a storage backend
    """

    store_type: typing.Optional[StorageBackendStoreType] = pydantic.Field(default=None)
    """
    The generic Storage Backend type. Used to identify the required workflow for reading and writing media. Any `store_product` should be compatible, as much is required for basic interoperability between TAMS implementations, with their associated generic `store_type`.
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cloud (or other) provider of the Storage Backend
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region in the cloud this Storage Backend resides
    """

    availability_zone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The availability zone in the cloud region this Storage Backend resides. Note that many cloud providers randomize availability zone identifiers such that they are consistent within a cloud account, but not necessarily between accounts. Caution should be exercised when using this parameter.
    """

    store_product: typing.Optional[str] = pydantic.Field(default=None)
    """
    The storage product name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
