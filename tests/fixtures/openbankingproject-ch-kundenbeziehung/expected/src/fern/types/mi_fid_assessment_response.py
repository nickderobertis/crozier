

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mi_fid_assessment_response_risk_profile import MiFidAssessmentResponseRiskProfile
from .mi_fid_assessment_response_suitability_rating import MiFidAssessmentResponseSuitabilityRating


class MiFidAssessmentResponse(UniversalBaseModel):
    assessment_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assessmentId"), pydantic.Field(alias="assessmentId")
    ] = None
    suitability_rating: typing_extensions.Annotated[
        typing.Optional[MiFidAssessmentResponseSuitabilityRating],
        FieldMetadata(alias="suitabilityRating"),
        pydantic.Field(alias="suitabilityRating"),
    ] = None
    risk_profile: typing_extensions.Annotated[
        typing.Optional[MiFidAssessmentResponseRiskProfile],
        FieldMetadata(alias="riskProfile"),
        pydantic.Field(alias="riskProfile"),
    ] = None
    approved_instruments: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="approvedInstruments"),
        pydantic.Field(alias="approvedInstruments"),
    ] = None
    restrictions: typing.Optional[typing.List[str]] = None
    valid_until: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="validUntil"), pydantic.Field(alias="validUntil")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
