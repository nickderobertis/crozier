

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id


class EcommerceProductVariantsItemImagesItem(UniversalBaseModel):
    id: typing.Optional[Id] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of an image of the variant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
