

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount
from .label_monetary_account import LabelMonetaryAccount
from .label_user import LabelUser


class RegistryMembership(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount of the user who belongs to this RegistryMembership.
    """

    auto_add_card_transaction: typing.Optional[str] = pydantic.Field(default=None)
    """
    The setting for for adding automatically card transactions to the registry.
    """

    balance: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The balance of this RegistryMembership.
    """

    invitor: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label of the user that sent the invite.
    """

    registry_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The registry id.
    """

    registry_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The registry title.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the RegistryMembership.
    """

    status_settlement: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the settlement of the Registry. Can be PENDING or SETTLED.
    """

    total_amount_spent: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount spent of this RegistryMembership.
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="The UUID of the membership."),
    ] = None
    """
    The UUID of the membership.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
