

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Location(UniversalBaseModel):
    fragments: typing.List[str]
    position: typing.Optional[int] = None
    progression: typing.Optional[float] = None
    total_progression: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="totalProgression"), pydantic.Field(alias="totalProgression")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
