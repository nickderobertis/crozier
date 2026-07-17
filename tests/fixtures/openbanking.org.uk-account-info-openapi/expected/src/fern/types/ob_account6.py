

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .active_or_historic_currency_code0 import ActiveOrHistoricCurrencyCode0
from .description0 import Description0
from .maturity_date import MaturityDate
from .nickname import Nickname
from .ob_account6account_item import ObAccount6AccountItem
from .ob_account_status1code import ObAccountStatus1Code
from .ob_branch_and_financial_institution_identification50 import ObBranchAndFinancialInstitutionIdentification50
from .ob_external_account_sub_type1code import ObExternalAccountSubType1Code
from .ob_external_account_type1code import ObExternalAccountType1Code
from .ob_external_switch_status_code import ObExternalSwitchStatusCode
from .opening_date import OpeningDate
from .status_update_date_time import StatusUpdateDateTime


class ObAccount6(UniversalBaseModel):
    """
    Unambiguous identification of the account to which credit and debit entries are made. The following fields are optional only for accounts that are switched:

      * Data.Currency
      * Data.AccountType
      * Data.AccountSubType

    For all other accounts, the fields must be populated by the ASPSP.
    """

    account: typing_extensions.Annotated[
        typing.Optional[typing.List[ObAccount6AccountItem]],
        FieldMetadata(alias="Account"),
        pydantic.Field(alias="Account"),
    ] = None
    account_id: typing_extensions.Annotated[
        AccountId, FieldMetadata(alias="AccountId"), pydantic.Field(alias="AccountId")
    ]
    account_sub_type: typing_extensions.Annotated[
        typing.Optional[ObExternalAccountSubType1Code],
        FieldMetadata(alias="AccountSubType"),
        pydantic.Field(alias="AccountSubType"),
    ] = None
    account_type: typing_extensions.Annotated[
        typing.Optional[ObExternalAccountType1Code],
        FieldMetadata(alias="AccountType"),
        pydantic.Field(alias="AccountType"),
    ] = None
    currency: typing_extensions.Annotated[
        typing.Optional[ActiveOrHistoricCurrencyCode0],
        FieldMetadata(alias="Currency"),
        pydantic.Field(alias="Currency"),
    ] = None
    description: typing_extensions.Annotated[
        typing.Optional[Description0], FieldMetadata(alias="Description"), pydantic.Field(alias="Description")
    ] = None
    maturity_date: typing_extensions.Annotated[
        typing.Optional[MaturityDate], FieldMetadata(alias="MaturityDate"), pydantic.Field(alias="MaturityDate")
    ] = None
    nickname: typing_extensions.Annotated[
        typing.Optional[Nickname], FieldMetadata(alias="Nickname"), pydantic.Field(alias="Nickname")
    ] = None
    opening_date: typing_extensions.Annotated[
        typing.Optional[OpeningDate], FieldMetadata(alias="OpeningDate"), pydantic.Field(alias="OpeningDate")
    ] = None
    servicer: typing_extensions.Annotated[
        typing.Optional[ObBranchAndFinancialInstitutionIdentification50],
        FieldMetadata(alias="Servicer"),
        pydantic.Field(alias="Servicer"),
    ] = None
    status: typing_extensions.Annotated[
        typing.Optional[ObAccountStatus1Code], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
    status_update_date_time: typing_extensions.Annotated[
        typing.Optional[StatusUpdateDateTime],
        FieldMetadata(alias="StatusUpdateDateTime"),
        pydantic.Field(alias="StatusUpdateDateTime"),
    ] = None
    switch_status: typing_extensions.Annotated[
        typing.Optional[ObExternalSwitchStatusCode],
        FieldMetadata(alias="SwitchStatus"),
        pydantic.Field(alias="SwitchStatus"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
