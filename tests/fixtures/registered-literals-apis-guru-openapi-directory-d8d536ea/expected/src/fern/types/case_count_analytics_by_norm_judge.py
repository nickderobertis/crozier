

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CaseCountAnalyticsByNormJudge(UniversalBaseModel):
    case_count: typing_extensions.Annotated[int, FieldMetadata(alias="caseCount"), pydantic.Field(alias="caseCount")]
    case_search_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseSearchAPI"),
        pydantic.Field(alias="caseSearchAPI", description="Link to cases for this criteria."),
    ]
    """
    Link to cases for this criteria.
    """

    norm_judge_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normJudgeId"), pydantic.Field(alias="normJudgeId")
    ]
    norm_judge_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="normJudgeName"), pydantic.Field(alias="normJudgeName")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
