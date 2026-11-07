

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VmLogsUploadInfo(UniversalBaseModel):
    container_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="containerName"), pydantic.Field(alias="containerName")
    ] = None
    message: typing.Optional[str] = None
    path_in_container: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pathInContainer"), pydantic.Field(alias="pathInContainer")
    ] = None
    storage_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="storageUri"), pydantic.Field(alias="storageUri")
    ] = None
    vm_resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="vmResourceId"), pydantic.Field(alias="vmResourceId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
