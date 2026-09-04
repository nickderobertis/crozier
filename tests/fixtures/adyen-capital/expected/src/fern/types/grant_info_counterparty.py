

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GrantInfoCounterparty(UniversalBaseModel):
    balance_account_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="balanceAccountId"),
        pydantic.Field(
            alias="balanceAccountId",
            description="The unique identifier of the balance account where the funds are disbursed. The balance account must belong to the specified account holder.",
        ),
    ] = None
    """
    The unique identifier of the balance account where the funds are disbursed. The balance account must belong to the specified account holder.
    """

    transfer_instrument_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transferInstrumentId"),
        pydantic.Field(
            alias="transferInstrumentId",
            description="The unique identifier of the transfer instrument where the funds are disbursed. The transfer instrument must belong to the legal entity of the specified account holder.",
        ),
    ] = None
    """
    The unique identifier of the transfer instrument where the funds are disbursed. The transfer instrument must belong to the legal entity of the specified account holder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
