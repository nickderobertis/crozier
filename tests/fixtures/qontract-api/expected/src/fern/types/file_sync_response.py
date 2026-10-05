

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_sync_status import FileSyncStatus


class FileSyncResponse(UniversalBaseModel):
    """
    Response from file sync reconciliation.
    """

    mr_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the created or existing merge request
    """

    status: FileSyncStatus = pydantic.Field()
    """
    Reconciliation outcome
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
