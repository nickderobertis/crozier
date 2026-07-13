

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinyComponentsKiosksDestinyKioskItem(UniversalBaseModel):
    can_acquire: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="canAcquire")] = pydantic.Field(
        default=None
    )
    """
    If true, the user can not only see the item, but they can acquire it. It is possible that a user can see a kiosk item and not be able to acquire it.
    """

    failure_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="failureIndexes")
    ] = pydantic.Field(default=None)
    """
    Indexes into failureStrings for the Vendor, indicating the reasons why it failed if any.
    """

    flavor_objective: typing_extensions.Annotated[
        typing.Optional[DestinyQuestsDestinyObjectiveProgress], FieldMetadata(alias="flavorObjective")
    ] = pydantic.Field(default=None)
    """
    I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for "flavor" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the item in the related DestinyVendorDefintion's itemList property, representing the sale.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
