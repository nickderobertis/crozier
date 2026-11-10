

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_risk_signal_institution_metadata import DocumentRiskSignalInstitutionMetadata


class DocumentRiskSignal(UniversalBaseModel):
    """
    Details about a certain reason as to why a document could potentially be fraudulent.
    """

    actual_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The derived value obtained in the risk signal calculation process for this field
    """

    expected_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The expected value of the field, as seen on the document
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field which the risk signal was computed for
    """

    has_fraud_risk: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A flag used to quickly identify if the signal indicates that this field is authentic or fraudulent
    """

    institution_metadata: typing.Optional[DocumentRiskSignalInstitutionMetadata] = None
    page_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    The relevant page associated with the risk signal
    """

    signal_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable explanation providing more detail into the particular risk signal
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The result from the risk signal check.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
