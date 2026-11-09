

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bar_record_preview import BarRecordPreview
from .case_timeline import CaseTimeline


class AssociatedNormAttorney(UniversalBaseModel):
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
    norm_attorney_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normAttorneyAPI"),
        pydantic.Field(alias="normAttorneyAPI", description="Link to details for the Attorney."),
    ]
    """
    Link to details for the Attorney.
    """

    norm_attorney_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyId"), pydantic.Field(alias="normAttorneyId")
    ]
    object: str
    state_bar_data_array: typing_extensions.Annotated[
        typing.List[BarRecordPreview],
        FieldMetadata(alias="stateBarDataArray"),
        pydantic.Field(alias="stateBarDataArray"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
