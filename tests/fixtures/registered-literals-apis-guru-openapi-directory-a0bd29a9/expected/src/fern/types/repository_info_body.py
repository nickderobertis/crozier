

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RepositoryInfoBody(UniversalBaseModel):
    branch_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="branchName"), pydantic.Field(alias="branchName")
    ] = None
    commit_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="commitId"), pydantic.Field(alias="commitId")
    ] = None
    create_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createType"), pydantic.Field(alias="createType")
    ] = None
    disk_usage: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="diskUsage"), pydantic.Field(alias="diskUsage")
    ] = None
    name: typing.Optional[str] = None
    owner: typing.Optional[str] = None
    prebuild_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="prebuildHash"), pydantic.Field(alias="prebuildHash")
    ] = None
    repo_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="repoId"), pydantic.Field(alias="repoId")
    ] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
