

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .multi_document_risk_signal import MultiDocumentRiskSignal
from .single_document_risk_signal import SingleDocumentRiskSignal


class DocumentRiskSignalsObject(UniversalBaseModel):
    """
    Object containing fraud risk data for a set of income documents.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the payroll provider account.
    """

    multi_document_risk_signals: typing.List[MultiDocumentRiskSignal] = pydantic.Field()
    """
    Array of risk signals computed from a set of uploaded documents and the associated documents' metadata
    """

    single_document_risk_signals: typing.List[SingleDocumentRiskSignal] = pydantic.Field()
    """
    Array of document metadata and associated risk signals per document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
