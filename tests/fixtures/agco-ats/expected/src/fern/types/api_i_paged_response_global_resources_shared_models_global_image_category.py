

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_paged_response_metadata import ApiPagedResponseMetadata
from .global_resources_shared_models_global_image_category import GlobalResourcesSharedModelsGlobalImageCategory


class ApiIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory(UniversalBaseModel):
    entities: typing_extensions.Annotated[
        typing.Optional[typing.List[GlobalResourcesSharedModelsGlobalImageCategory]],
        FieldMetadata(alias="Entities"),
        pydantic.Field(alias="Entities"),
    ] = None
    metadata: typing_extensions.Annotated[
        typing.Optional[ApiPagedResponseMetadata], FieldMetadata(alias="Metadata"), pydantic.Field(alias="Metadata")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
