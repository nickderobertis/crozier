

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImageSelector(UniversalBaseModel):
    """
    A set of selection criteria to match an image by a tagged pullstring based on its components, with regex support in each field
    """

    registry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The registry section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "docker.io"
    """

    repository: typing.Optional[str] = pydantic.Field(default=None)
    """
    The repository section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "anchore/anchore-engine"
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tag-only section of a pull string. e.g. with "docker.io/anchore/anchore-engine:latest", this is "latest"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
