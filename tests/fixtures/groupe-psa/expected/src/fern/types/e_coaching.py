

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .e_coaching_links import ECoachingLinks
from .e_coaching_scores_item import ECoachingScoresItem


class ECoaching(UniversalBaseModel):
    links: typing_extensions.Annotated[ECoachingLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    scores: typing.Optional[typing.List[ECoachingScoresItem]] = None
    embedded: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="_embedded"),
        pydantic.Field(alias="_embedded"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
