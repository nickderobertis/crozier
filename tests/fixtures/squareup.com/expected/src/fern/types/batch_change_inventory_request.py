

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inventory_change import InventoryChange


class BatchChangeInventoryRequest(UniversalBaseModel):
    """ """

    changes: typing.Optional[typing.List[InventoryChange]] = pydantic.Field(default=None)
    """
    The set of physical counts and inventory adjustments to be made.
    Changes are applied based on the client-supplied timestamp and may be sent
    out of order.
    """

    idempotency_key: str = pydantic.Field()
    """
    A client-supplied, universally unique identifier (UUID) for the
    request.
    
    See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) in the
    [API Development 101](https://developer.squareup.com/docs/basics/api101/overview) section for more
    information.
    """

    ignore_unchanged_counts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the current physical count should be ignored if
    the quantity is unchanged since the last physical count. Default: `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
