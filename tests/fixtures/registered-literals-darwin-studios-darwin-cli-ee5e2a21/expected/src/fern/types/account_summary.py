

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_summary_account import AccountSummaryAccount
from .account_summary_active_ai import AccountSummaryActiveAi
from .account_summary_ais_item import AccountSummaryAisItem


class AccountSummary(UniversalBaseModel):
    account: AccountSummaryAccount
    ais: typing.List[AccountSummaryAisItem]
    active_ai: typing_extensions.Annotated[
        typing.Optional[AccountSummaryActiveAi], FieldMetadata(alias="activeAi"), pydantic.Field(alias="activeAi")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
