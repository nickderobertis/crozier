

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .active_or_historic_currency_code0 import ActiveOrHistoricCurrencyCode0
from .description0 import Description0
from .nickname import Nickname
from .ob_account_status1code import ObAccountStatus1Code
from .ob_external_account_sub_type1code import ObExternalAccountSubType1Code
from .ob_external_account_type1code import ObExternalAccountType1Code
from .status_update_date_time import StatusUpdateDateTime


class ObAccount4Basic(UniversalBaseModel):
    """
    Unambiguous identification of the account to which credit and debit entries are made.
    """

    account_id: typing_extensions.Annotated[AccountId, FieldMetadata(alias="AccountId")]
    account_sub_type: typing_extensions.Annotated[ObExternalAccountSubType1Code, FieldMetadata(alias="AccountSubType")]
    account_type: typing_extensions.Annotated[ObExternalAccountType1Code, FieldMetadata(alias="AccountType")]
    currency: typing_extensions.Annotated[ActiveOrHistoricCurrencyCode0, FieldMetadata(alias="Currency")]
    description: typing_extensions.Annotated[typing.Optional[Description0], FieldMetadata(alias="Description")] = None
    nickname: typing_extensions.Annotated[typing.Optional[Nickname], FieldMetadata(alias="Nickname")] = None
    status: typing_extensions.Annotated[typing.Optional[ObAccountStatus1Code], FieldMetadata(alias="Status")] = None
    status_update_date_time: typing_extensions.Annotated[
        typing.Optional[StatusUpdateDateTime], FieldMetadata(alias="StatusUpdateDateTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
