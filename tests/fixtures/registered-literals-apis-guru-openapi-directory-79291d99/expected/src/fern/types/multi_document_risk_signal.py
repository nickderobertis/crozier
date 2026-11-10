

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_risk_signal import DocumentRiskSignal
from .risk_signal_document_reference import RiskSignalDocumentReference


class MultiDocumentRiskSignal(UniversalBaseModel):
    """
    Object containing risk signals and relevant metadata for a set of uploaded documents
    """

    document_references: typing.List[RiskSignalDocumentReference] = pydantic.Field()
    """
    Array of objects containing attributes that could indicate if a document is fraudulent
    """

    risk_signals: typing.List[typing.Optional[DocumentRiskSignal]] = pydantic.Field()
    """
    Array of attributes that indicate whether or not there is fraud risk with a set of documents
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
