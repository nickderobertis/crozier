

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImageImage(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    The publicly accessible URL of the image attachment. The image file is available for 48 hours after it is created. Supported types are .jpg, .jpeg, and .png
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
