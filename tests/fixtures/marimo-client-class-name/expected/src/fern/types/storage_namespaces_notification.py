

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .storage_namespace import StorageNamespace
from .storage_namespaces_notification_op import StorageNamespacesNotificationOp


class StorageNamespacesNotification(UniversalBaseModel):
    """
    Available storage namespaces for storage inspector.

        Attributes:
            namespaces: Available storage namespaces.
    """

    namespaces: typing.List[StorageNamespace]
    op: StorageNamespacesNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
