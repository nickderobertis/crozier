

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .electronic_record_created_at import ElectronicRecordCreatedAt
from .electronic_record_date_of_expiry import ElectronicRecordDateOfExpiry
from .evidence_issuer import EvidenceIssuer
from .filter_criteria import FilterCriteria


class ElectronicRecord(UniversalBaseModel):
    """
    JSON object representing the record used to perform the identity verification. It consists of the following properties:
    """

    type: typing.Optional[FilterCriteria] = pydantic.Field(default=None)
    """
    String denoting the type of electronic record. 
    """

    personal_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    String representing an identifier that is assigned to the End-User and is not limited to being used in one record, for example a national identification number, personal identity number, citizen number, social security number, driver number, account number, customer number, licensee number, etc.
    """

    created_at: typing.Optional[ElectronicRecordCreatedAt] = None
    date_of_expiry: typing.Optional[ElectronicRecordDateOfExpiry] = None
    source: typing.Optional[EvidenceIssuer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
