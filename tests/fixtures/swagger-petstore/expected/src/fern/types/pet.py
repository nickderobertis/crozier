

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .category import Category
from .pet_status import PetStatus
from .tag import Tag


class Pet(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: str
    category: typing.Optional[Category] = None
    photo_urls: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="photoUrls"), pydantic.Field(alias="photoUrls")
    ]
    tags: typing.Optional[typing.List[Tag]] = None
    status: typing.Optional[PetStatus] = pydantic.Field(default=None)
    """
    pet status in the store
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
