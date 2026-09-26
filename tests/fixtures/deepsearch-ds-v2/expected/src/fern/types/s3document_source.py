

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .s3coordinates import S3Coordinates


class S3DocumentSource(UniversalBaseModel):
    """
    Specifies documents to import from an S3 bucket
    """

    coordinates: S3Coordinates
    object_keys: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of s3 object keys to retrieve from bucket to be converted and uploaded to the data index.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
