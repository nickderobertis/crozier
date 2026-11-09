

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .matched_object import MatchedObject


class NormJudgeSearchResult(UniversalBaseModel):
    first_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="firstFetchDate"), pydantic.Field(alias="firstFetchDate")
    ]
    last_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastFetchDate"), pydantic.Field(alias="lastFetchDate")
    ]
    matched_object_array: typing_extensions.Annotated[
        typing.List[typing.Optional[MatchedObject]],
        FieldMetadata(alias="matchedObjectArray"),
        pydantic.Field(alias="matchedObjectArray"),
    ]
    name: str
    norm_judge_details_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="normJudgeDetailsAPI"), pydantic.Field(alias="normJudgeDetailsAPI")
    ]
    norm_judge_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normJudgeId"), pydantic.Field(alias="normJudgeId")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
