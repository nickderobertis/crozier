

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AnalysisArchiveSummary(UniversalBaseModel):
    """
    A summarization of the analysis archive, including size, counts, etc. This archive stores image analysis only, never the actual image content or layers.
    """

    last_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of the most recent archived image
    """

    total_data_bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total sum of all the bytes stored to the backing storage. Accounts for anchore-applied compression, but not compression by the underlying storage system.
    """

    total_image_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unique images (digests) in the archive
    """

    total_tag_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of tag records (registry/repo:tag pull strings) in the archive. This may include repeated tags but will always have a unique tag->digest mapping per record.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
