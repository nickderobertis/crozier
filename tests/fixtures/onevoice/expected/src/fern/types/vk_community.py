

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VkCommunity(UniversalBaseModel):
    id: int
    name: str
    screen_name: str
    photo50: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="photo_50"), pydantic.Field(alias="photo_50")
    ] = None
    members_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
