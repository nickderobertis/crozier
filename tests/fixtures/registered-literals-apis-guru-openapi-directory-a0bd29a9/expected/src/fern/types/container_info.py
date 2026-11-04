

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContainerInfo(UniversalBaseModel):
    id: typing.Optional[str] = None
    image_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageName"), pydantic.Field(alias="imageName")
    ] = None
    schema_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schemaVersion"), pydantic.Field(alias="schemaVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
