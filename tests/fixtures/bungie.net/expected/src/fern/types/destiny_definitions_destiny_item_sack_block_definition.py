

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemSackBlockDefinition(UniversalBaseModel):
    """
    Some items are "sacks" - they can be "opened" to produce other items. This is information related to its sack status, mostly UI strings. Engrams are an example of items that are considered to be "Sacks".
    """

    detail_action: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="detailAction")] = (
        pydantic.Field(default=None)
    )
    """
    A description of what will happen when you open the sack. As far as I can tell, this is blank currently. Unknown whether it will eventually be populated with useful info.
    """

    open_action: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="openAction")] = pydantic.Field(
        default=None
    )
    """
    The localized name of the action being performed when you open the sack.
    """

    open_on_acquire: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="openOnAcquire")] = None
    select_item_count: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="selectItemCount")] = None
    vendor_sack_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="vendorSackType")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
