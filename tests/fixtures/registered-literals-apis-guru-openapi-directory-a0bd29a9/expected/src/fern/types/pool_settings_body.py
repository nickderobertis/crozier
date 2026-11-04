

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pool import Pool
from .storage_type import StorageType


class PoolSettingsBody(UniversalBaseModel):
    branch_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="branchName"), pydantic.Field(alias="branchName")
    ] = None
    dev_container_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="devContainerPath"), pydantic.Field(alias="devContainerPath")
    ] = None
    pools: typing.Optional[typing.List[Pool]] = None
    repo_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="repoId"), pydantic.Field(alias="repoId")
    ] = None
    storage_type: typing_extensions.Annotated[
        typing.Optional[StorageType], FieldMetadata(alias="storageType"), pydantic.Field(alias="storageType")
    ] = None
    subscription: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
