

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .atlas_entity import AtlasEntity


class AtlasEntityWithExtInfo(UniversalBaseModel):
    referred_entities: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, AtlasEntity]],
        FieldMetadata(alias="referredEntities"),
        pydantic.Field(alias="referredEntities"),
    ] = None
    entity: typing.Optional[AtlasEntity] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
