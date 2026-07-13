

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyMilestonesDestinyMilestoneContentItemCategory(UniversalBaseModel):
    """
    Part of our dynamic, localized Milestone content is arbitrary categories of items. These are built in our content management system, and thus aren't the same as programmatically generated rewards.
    """

    item_hashes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="itemHashes")] = (
        None
    )
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
