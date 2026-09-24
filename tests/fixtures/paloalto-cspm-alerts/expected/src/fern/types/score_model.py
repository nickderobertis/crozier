

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScoreModel(UniversalBaseModel):
    """
    Model for Score
    """

    max_score: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxScore"), pydantic.Field(alias="maxScore", description="Max Score")
    ] = None
    """
    Max Score
    """

    score: typing.Optional[int] = pydantic.Field(default=None)
    """
    Score
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
