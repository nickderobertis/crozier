

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_dex_pools_response_pools_item_quote_observation_parameters_value import (
    GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservationParametersValue,
)


class GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservation(UniversalBaseModel):
    """
    Quote conversion captured with the pool snapshot. Null for older observations. A fixed USDG notional assumption has no oracle source timestamp.
    """

    value: typing.Optional[float] = None
    source: typing.Optional[str] = None
    reason: typing.Optional[str] = None
    source_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceId"),
        pydantic.Field(
            alias="sourceId",
            description="Stable source kind and identity; null when the stored source has no structured identity.",
        ),
    ] = None
    """
    Stable source kind and identity; null when the stored source has no structured identity.
    """

    source_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="sourceAt"), pydantic.Field(alias="sourceAt")
    ] = None
    fetched_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="fetchedAt"), pydantic.Field(alias="fetchedAt")
    ] = None
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    block_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blockNumber"), pydantic.Field(alias="blockNumber")
    ] = None
    block_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blockHash"), pydantic.Field(alias="blockHash")
    ] = None
    method: str
    parameters: typing.Dict[
        str, typing.Optional[GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservationParametersValue]
    ] = pydantic.Field()
    """
    Structured computation parameters, including historical quote sampling/oracle times and valuation assumptions when recorded.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
