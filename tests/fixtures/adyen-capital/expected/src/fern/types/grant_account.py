

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .balance import Balance
from .grant_limit import GrantLimit


class GrantAccount(UniversalBaseModel):
    balances: typing.Optional[typing.List[Balance]] = pydantic.Field(default=None)
    """
    Contains the sum of the balances of all grants tracked by this grant account. The balances are separated by currency.
    """

    funding_balance_account_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fundingBalanceAccountId"),
        pydantic.Field(
            alias="fundingBalanceAccountId",
            description="The unique identifier of the balance account used to fund the grant.",
        ),
    ] = None
    """
    The unique identifier of the balance account used to fund the grant.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the grant account.
    """

    limits: typing.Optional[typing.List[GrantLimit]] = pydantic.Field(default=None)
    """
    Contains the maximum amount of funds that you can disburse for grants.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
