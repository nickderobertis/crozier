

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_equip_item_result import DestinyDestinyEquipItemResult


class DestinyDestinyEquipItemResults(UniversalBaseModel):
    """
    The results of a bulk Equipping operation performed through the Destiny API.
    """

    equip_results: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyEquipItemResult]],
        FieldMetadata(alias="equipResults"),
        pydantic.Field(alias="equipResults"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
