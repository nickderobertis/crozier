

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .storage_download_ready_notification_op import StorageDownloadReadyNotificationOp


class StorageDownloadReadyNotification(UniversalBaseModel):
    """
    Signals that a storage file download is ready.

        The url may be a signed cloud URL (preferred) or a virtual file URL
        (fallback for backends that don't support signing).

        Attributes:
            request_id: Request ID this responds to.
            url: Signed or virtual-file URL to download from.
            filename: Suggested filename for the download.
            error: Error message if the download failed.
    """

    error: typing.Optional[str] = None
    filename: typing.Optional[str] = None
    op: StorageDownloadReadyNotificationOp
    request_id: str
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
