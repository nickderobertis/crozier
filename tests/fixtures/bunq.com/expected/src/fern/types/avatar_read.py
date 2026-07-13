

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .image import Image


class AvatarRead(UniversalBaseModel):
    image: typing.Optional[typing.List[Image]] = pydantic.Field(default=None)
    """
    The content type of the image.
    """

    uuid_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uuid")] = pydantic.Field(default=None)
    """
    The UUID of the created avatar.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
