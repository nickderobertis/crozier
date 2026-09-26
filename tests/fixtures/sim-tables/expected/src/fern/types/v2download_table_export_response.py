

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2table_export_download_data import V2TableExportDownloadData


class V2DownloadTableExportResponse(UniversalBaseModel):
    """
    Short-lived signed URL, filename, and expiration timestamp.
    """

    data: V2TableExportDownloadData = pydantic.Field()
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
