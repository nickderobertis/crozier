

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_timeline import CaseTimeline


class AssociatedNormJudge(UniversalBaseModel):
    """
    Associated Judge
    """

    case_count: typing_extensions.Annotated[int, FieldMetadata(alias="caseCount"), pydantic.Field(alias="caseCount")]
    case_search_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseSearchAPI"),
        pydantic.Field(alias="caseSearchAPI", description="Link to related cases for this association."),
    ]
    """
    Link to related cases for this association.
    """

    case_timeline: typing_extensions.Annotated[
        CaseTimeline, FieldMetadata(alias="caseTimeline"), pydantic.Field(alias="caseTimeline")
    ]
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    middle_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="middleName"), pydantic.Field(alias="middleName")
    ] = None
    name: str
    norm_judge_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normJudgeAPI"),
        pydantic.Field(alias="normJudgeAPI", description="Link to Details from the Judge."),
    ]
    """
    Link to Details from the Judge.
    """

    norm_judge_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normJudgeId"), pydantic.Field(alias="normJudgeId")
    ]
    object: str
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
