

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity_transaction_response_error import EntityTransactionResponseError
from .entity_transaction_response_failed_item import EntityTransactionResponseFailedItem


class EntityTransactionResponse(UniversalBaseModel):
    """
    Response element returned by entity create/update operations. The
    wire response is always an array of these elements, with one
    element per transactional batch in commit order.

    For collection endpoints the request may be split into multiple
    chunks of up to `transactionWindow` items each. Successful chunks
    carry `transactionId` + `entityIds`. If a later chunk fails after
    earlier chunks have committed, the failure surfaces as an element
    carrying the `error` object (with `chunkIndex` set to the failing
    chunk's zero-based position) instead of `transactionId` and
    `entityIds`. Earlier chunks remain durable.

    cyoda-go extension #228 (not yet in Cloud): per-item
    ENTITY_MODIFIED conflicts on UpdateCollection items carrying
    `ifMatch` surface inside the `200` response body via the
    `failed[]` array, not as a `4xx` envelope. Inspect `failed[]` to
    detect them. The `4xx` envelope is reserved for chunk-wide
    infrastructure failures (malformed JSON, missing entity,
    validation failure, non-conflict engine error).
    """

    transaction_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transactionId"), pydantic.Field(alias="transactionId")
    ] = None
    entity_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="entityIds"),
        pydantic.Field(alias="entityIds"),
    ] = None
    error: typing.Optional[EntityTransactionResponseError] = pydantic.Field(default=None)
    """
    Present only on chunk-failure elements. Absent on successful
    elements (which carry `transactionId` + `entityIds`).
    """

    failed: typing.Optional[typing.List[EntityTransactionResponseFailedItem]] = pydantic.Field(default=None)
    """
    cyoda-go extension #228 (not yet in Cloud). Present only on
    UpdateCollection chunks where one or more items carrying an
    `ifMatch` precondition failed with ENTITY_MODIFIED. The chunk
    still commits its successful siblings; the conflicted items
    surface here without rolling the chunk back.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
