

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bunq_id import BunqId


class CardBatchReplaceCreate(UniversalBaseModel):
    updated_card_ids: typing.Optional[typing.List[BunqId]] = pydantic.Field(default=None)
    """
    The ids of the cards that have been replaced.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
