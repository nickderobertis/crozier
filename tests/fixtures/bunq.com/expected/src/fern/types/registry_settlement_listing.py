

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .registry_membership import RegistryMembership
from .registry_settlement_item import RegistrySettlementItem


class RegistrySettlementListing(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the RegistrySettlement's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the RegistrySettlement.
    """

    items: typing.Optional[typing.List[RegistrySettlementItem]] = pydantic.Field(default=None)
    """
    List of RegistrySettlementItems
    """

    membership_settled: typing.Optional[RegistryMembership] = pydantic.Field(default=None)
    """
    The membership of the user that has settled the registry.
    """

    number_of_entries: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of RegistryEntry's associated with this RegistrySettlement.
    """

    settled_by_alias: typing.Optional[RegistryMembership] = pydantic.Field(default=None)
    """
    The membership of the user that settled the Registry.
    """

    settlement_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the Registry's settlement.
    """

    total_amount_spent: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount spent for the RegistrySettlement.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the RegistrySettlement's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
