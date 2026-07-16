

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Gzip(UniversalBaseModel):
    """
    Configuration for gzip of service responses
    """

    black_list: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="blackList")] = pydantic.Field()
    """
    Blacklisted mime types. Wildcard supported
    """

    buffer_size: typing_extensions.Annotated[int, FieldMetadata(alias="bufferSize")] = pydantic.Field()
    """
    Size of the GZip buffer
    """

    chunked_threshold: typing_extensions.Annotated[int, FieldMetadata(alias="chunkedThreshold")] = pydantic.Field()
    """
    Threshold for chunking data
    """

    compression_level: typing_extensions.Annotated[int, FieldMetadata(alias="compressionLevel")] = pydantic.Field()
    """
    Compression level. From 0 to 9
    """

    enabled: bool = pydantic.Field()
    """
    Whether gzip compression is enabled or not
    """

    excluded_patterns: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="excludedPatterns")] = (
        pydantic.Field()
    )
    """
    Patterns that are excluded from gzipping
    """

    white_list: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="whiteList")] = pydantic.Field()
    """
    Whitelisted mime types. Wildcard supported
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
