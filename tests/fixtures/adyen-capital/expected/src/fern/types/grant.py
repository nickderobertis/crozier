

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .balance import Balance
from .grant_counterparty import GrantCounterparty
from .status import Status


class Grant(UniversalBaseModel):
    balances: Balance = pydantic.Field()
    """
    Contains information about the balances of the grant.
    """

    counterparty: typing.Optional[GrantCounterparty] = pydantic.Field(default=None)
    """
    Contains the details of the party that receives the grant.
    """

    grant_account_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="grantAccountId"),
        pydantic.Field(
            alias="grantAccountId", description="The unique identifier of the grant account that tracks this grant."
        ),
    ]
    """
    The unique identifier of the grant account that tracks this grant.
    """

    grant_offer_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="grantOfferId"),
        pydantic.Field(
            alias="grantOfferId",
            description="The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.",
        ),
    ]
    """
    The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of the grant reference.
    """

    status: Status = pydantic.Field()
    """
    Contains the status of the grant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
