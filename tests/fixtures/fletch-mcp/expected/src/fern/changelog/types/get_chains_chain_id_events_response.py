

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_events_response_events_item import GetChainsChainIdEventsResponseEventsItem


class GetChainsChainIdEventsResponse(UniversalBaseModel):
    events: typing.List[GetChainsChainIdEventsResponseEventsItem]
    kinds: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Every kind the daemon can emit; present only on the newest-first read (no `since`/`cursor`)
    """

    next_cursor: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(
            alias="nextCursor",
            description="`${observedAt}|${id}` of the last row seen; pass it back as `cursor` to receive only what follows. The epoch when the changelog is empty.",
        ),
    ]
    """
    `${observedAt}|${id}` of the last row seen; pass it back as `cursor` to receive only what follows. The epoch when the changelog is empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
