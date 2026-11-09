

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_count_analytics_by_court_system_geo import CaseCountAnalyticsByCourtSystemGeo
from .court_system import CourtSystem


class CaseCountAnalyticsByCourtSystem(UniversalBaseModel):
    geo: typing_extensions.Annotated[
        typing.Optional[CaseCountAnalyticsByCourtSystemGeo], FieldMetadata(alias="Geo"), pydantic.Field(alias="Geo")
    ] = None
    case_count: typing_extensions.Annotated[int, FieldMetadata(alias="caseCount"), pydantic.Field(alias="caseCount")]
    case_search_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseSearchAPI"),
        pydantic.Field(alias="caseSearchAPI", description="link to cases for this criteria."),
    ]
    """
    link to cases for this criteria.
    """

    court_system: typing_extensions.Annotated[
        CourtSystem, FieldMetadata(alias="courtSystem"), pydantic.Field(alias="courtSystem")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
