

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistryDigestSource(UniversalBaseModel):
    """
    An image reference using a digest in a registry, includes some extra tag and timestamp info in addition to the pull string to allow proper tag history reconstruction.
    """

    creation_timestamp_override: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Optional override of the image creation time to support proper tag history construction in cases of out-of-order analysis compared to registry history for the tag
    """

    dockerfile: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64 encoded content of the dockerfile used to build the image, if available.
    """

    pullstring: str = pydantic.Field()
    """
    A digest-based pullstring (e.g. docker.io/nginx@sha256:123abc)
    """

    tag: str = pydantic.Field()
    """
    A valid docker tag reference (e.g. docker.io/nginx:latest) that will be associated with the image but not used to pull the image.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
