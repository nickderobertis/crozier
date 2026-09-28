

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .labels import Labels


class Insight(UniversalBaseModel):
    is_verified: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isVerified"), pydantic.Field(alias="isVerified")
    ] = None
    labels: typing.List[Labels]
    owner: str
    stars: float
    usage: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
