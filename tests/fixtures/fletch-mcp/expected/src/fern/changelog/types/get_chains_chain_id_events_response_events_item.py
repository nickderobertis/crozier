

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetChainsChainIdEventsResponseEventsItem(UniversalBaseModel):
    """
    One entry in the registry changelog. `id` is stable across re-runs; the cursor for the row is `${observedAt}|${id}`.
    """

    id: str = pydantic.Field()
    """
    `ev_` followed by 24 hex characters; the same change is never written twice
    """

    kind: str = pydantic.Field()
    """
    A dotted kind such as `registry.paused` or `multiplier.applied`; every kind the daemon can emit is in the response's `kinds`
    """

    title: str = pydantic.Field()
    """
    The change as one changelog line
    """

    symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    The token concerned; null for a chain-wide event
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The contract or account concerned; null for a chain-wide event
    """

    detail: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The numbers behind the title; fields depend on the kind
    """

    block: typing.Optional[str] = pydantic.Field(default=None)
    """
    Block number as a decimal string; null for events not tied to a block
    """

    tx_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="txHash"), pydantic.Field(alias="txHash")
    ] = None
    occurred_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="occurredAt"),
        pydantic.Field(alias="occurredAt", description="When the change happened on chain or at the source"),
    ]
    """
    When the change happened on chain or at the source
    """

    observed_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="observedAt"),
        pydantic.Field(alias="observedAt", description="When the daemon recorded it; the cursor orders by this"),
    ]
    """
    When the daemon recorded it; the cursor orders by this
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
