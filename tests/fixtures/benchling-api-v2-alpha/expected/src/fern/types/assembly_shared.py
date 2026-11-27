

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assembly_shared_assembly_type import AssemblySharedAssemblyType


class AssemblyShared(UniversalBaseModel):
    assembly_type: typing_extensions.Annotated[
        typing.Optional[AssemblySharedAssemblyType],
        FieldMetadata(alias="assemblyType"),
        pydantic.Field(alias="assemblyType"),
    ] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
