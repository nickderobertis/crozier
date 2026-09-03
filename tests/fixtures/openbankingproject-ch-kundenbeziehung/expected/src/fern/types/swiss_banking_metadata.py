

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .swiss_banking_metadata_support import SwissBankingMetadataSupport
from .swiss_banking_metadata_supported_banking_use_cases_item import SwissBankingMetadataSupportedBankingUseCasesItem


class SwissBankingMetadata(UniversalBaseModel):
    issuer: str
    swiss_open_banking_version: str
    kundenbeziehung_api_version: typing.Optional[str] = None
    supported_standards: typing.Optional[typing.List[str]] = None
    finma_compliance: typing.Optional[bool] = None
    dsg_compliance: typing.Optional[bool] = None
    gdpr_compliance: typing.Optional[bool] = None
    supported_banking_use_cases: typing.Optional[typing.List[SwissBankingMetadataSupportedBankingUseCasesItem]] = None
    supported_data_categories: typing.Optional[typing.List[str]] = None
    referenzprozess_steps: typing.Optional[typing.List[str]] = None
    technical_features: typing.Optional[typing.List[str]] = None
    support: typing.Optional[SwissBankingMetadataSupport] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
