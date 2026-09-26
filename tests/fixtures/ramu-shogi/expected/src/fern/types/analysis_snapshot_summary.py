

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AnalysisSnapshotSummary(UniversalBaseModel):
    id: str
    game_id: typing_extensions.Annotated[str, FieldMetadata(alias="gameId"), pydantic.Field(alias="gameId")]
    label: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    entry_count: typing_extensions.Annotated[int, FieldMetadata(alias="entryCount"), pydantic.Field(alias="entryCount")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
