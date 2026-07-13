

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyDefinitionsRecordsDestinyRecordIntervalRewards(UniversalBaseModel):
    interval_reward_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyItemQuantity]], FieldMetadata(alias="intervalRewardItems")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
