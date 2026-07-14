

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistryTagSource(UniversalBaseModel):
    """
    An image reference using a tag in a registry, this is the most common source type.
    """

    dockerfile: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64 encoded content of the dockerfile used to build the image, if available.
    """

    pullstring: str = pydantic.Field()
    """
    A docker pull string (e.g. docker.io/nginx:latest, or docker.io/nginx@sha256:abd) to retrieve the image
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
