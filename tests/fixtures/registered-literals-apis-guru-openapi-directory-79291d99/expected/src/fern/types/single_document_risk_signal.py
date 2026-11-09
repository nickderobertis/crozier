

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_risk_signal import DocumentRiskSignal
from .document_risk_summary import DocumentRiskSummary
from .risk_signal_document_reference import RiskSignalDocumentReference


class SingleDocumentRiskSignal(UniversalBaseModel):
    """
    Object containing all risk signals and relevant metadata for a single document
    """

    document_reference: RiskSignalDocumentReference
    risk_signals: typing.List[typing.Optional[DocumentRiskSignal]] = pydantic.Field()
    """
    Array of attributes that indicate whether or not there is fraud risk with a document
    """

    risk_summary: DocumentRiskSummary

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
