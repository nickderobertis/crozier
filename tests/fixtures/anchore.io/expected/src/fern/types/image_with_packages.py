

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_reference import ImageReference
from .package_reference import PackageReference


class ImageWithPackages(UniversalBaseModel):
    """
    An image record that contains packages
    """

    image: typing.Optional[ImageReference] = None
    packages: typing.Optional[typing.List[PackageReference]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
