

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsLoadoutsDestinyLoadoutItemComponent(UniversalBaseModel):
    item_instance_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="itemInstanceId"), pydantic.Field(alias="itemInstanceId")
    ] = None
    plug_item_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="plugItemHashes"), pydantic.Field(alias="plugItemHashes")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
