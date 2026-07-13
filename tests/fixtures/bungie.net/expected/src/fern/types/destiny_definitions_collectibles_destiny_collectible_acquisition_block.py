

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsCollectiblesDestinyCollectibleAcquisitionBlock(UniversalBaseModel):
    acquire_material_requirement_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="acquireMaterialRequirementHash")
    ] = None
    acquire_timestamp_unlock_value_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="acquireTimestampUnlockValueHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
