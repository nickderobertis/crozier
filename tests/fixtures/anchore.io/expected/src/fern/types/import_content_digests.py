

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImportContentDigests(UniversalBaseModel):
    """
    Digest of content to use in the final import
    """

    dockerfile: typing.Optional[str] = pydantic.Field(default=None)
    """
    Digest for reference content for dockerfile
    """

    image_config: str = pydantic.Field()
    """
    Digest for reference content for image config
    """

    manifest: str = pydantic.Field()
    """
    Digest to reference content for the image manifest
    """

    packages: str = pydantic.Field()
    """
    Digest to use for the packages content
    """

    parent_manifest: typing.Optional[str] = pydantic.Field(default=None)
    """
    Digest for reference content for parent manifest
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
