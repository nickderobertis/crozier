

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_reference import ImageReference
from .vulnerable_package_reference import VulnerablePackageReference


class VulnerableImage(UniversalBaseModel):
    """
    A record of an image vulnerable to some known vulnerability. Includes vulnerable package information
    """

    affected_packages: typing.Optional[typing.List[VulnerablePackageReference]] = None
    image: typing.Optional[ImageReference] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
