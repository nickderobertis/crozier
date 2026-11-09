

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_timeline import CaseTimeline
from .sos_data_preview import SosDataPreview


class AssociatedNormLawFirm(UniversalBaseModel):
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
    name: str
    norm_law_firm_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normLawFirmAPI"),
        pydantic.Field(alias="normLawFirmAPI", description="Link to Details for this Law Firm."),
    ]
    """
    Link to Details for this Law Firm.
    """

    norm_law_firm_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normLawFirmId"), pydantic.Field(alias="normLawFirmId")
    ]
    object: str
    sos_data_array: typing_extensions.Annotated[
        typing.List[SosDataPreview], FieldMetadata(alias="sosDataArray"), pydantic.Field(alias="sosDataArray")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
