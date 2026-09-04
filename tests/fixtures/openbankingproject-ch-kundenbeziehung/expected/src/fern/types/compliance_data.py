

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .compliance_data_aml_risk_rating import ComplianceDataAmlRiskRating
from .compliance_data_fatca_status import ComplianceDataFatcaStatus
from .screening_result import ScreeningResult
from .tax_residency import TaxResidency
from .tin_number import TinNumber


class ComplianceData(UniversalBaseModel):
    fatca_status: typing_extensions.Annotated[
        typing.Optional[ComplianceDataFatcaStatus],
        FieldMetadata(alias="fatcaStatus"),
        pydantic.Field(alias="fatcaStatus"),
    ] = None
    fatca_classification: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fatcaClassification"),
        pydantic.Field(alias="fatcaClassification", description="FATCA-Klassifikation"),
    ] = None
    """
    FATCA-Klassifikation
    """

    crs_reportable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="crsReportable"),
        pydantic.Field(alias="crsReportable", description="CRS-Meldepflicht"),
    ] = None
    """
    CRS-Meldepflicht
    """

    tax_residencies: typing_extensions.Annotated[
        typing.Optional[typing.List[TaxResidency]],
        FieldMetadata(alias="taxResidencies"),
        pydantic.Field(alias="taxResidencies"),
    ] = None
    tin_numbers: typing_extensions.Annotated[
        typing.Optional[typing.List[TinNumber]], FieldMetadata(alias="tinNumbers"), pydantic.Field(alias="tinNumbers")
    ] = None
    sanctions_screening: typing_extensions.Annotated[
        typing.Optional[ScreeningResult],
        FieldMetadata(alias="sanctionsScreening"),
        pydantic.Field(alias="sanctionsScreening"),
    ] = None
    aml_risk_rating: typing_extensions.Annotated[
        typing.Optional[ComplianceDataAmlRiskRating],
        FieldMetadata(alias="amlRiskRating"),
        pydantic.Field(alias="amlRiskRating"),
    ] = None
    last_due_diligence: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastDueDiligence"), pydantic.Field(alias="lastDueDiligence")
    ] = None
    next_review_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="nextReviewDate"), pydantic.Field(alias="nextReviewDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
