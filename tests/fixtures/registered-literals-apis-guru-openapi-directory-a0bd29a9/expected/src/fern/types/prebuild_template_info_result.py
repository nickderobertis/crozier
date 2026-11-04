

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PrebuildTemplateInfoResult(UniversalBaseModel):
    branch_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="branchName"), pydantic.Field(alias="branchName")
    ] = None
    commit_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="commitId"), pydantic.Field(alias="commitId")
    ] = None
    devcontainer_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="devcontainerPath"), pydantic.Field(alias="devcontainerPath")
    ] = None
    id: typing.Optional[str] = None
    is_prebuild: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPrebuild"), pydantic.Field(alias="isPrebuild")
    ] = None
    last_used_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUsedTime"), pydantic.Field(alias="lastUsedTime")
    ] = None
    logical_skus: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="logicalSkus"), pydantic.Field(alias="logicalSkus")
    ] = None
    prebuild_configuration_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="prebuildConfigurationId"),
        pydantic.Field(alias="prebuildConfigurationId"),
    ] = None
    prebuild_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="prebuildHash"), pydantic.Field(alias="prebuildHash")
    ] = None
    repo_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="repoId"), pydantic.Field(alias="repoId")
    ] = None
    template_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="templateStatus"), pydantic.Field(alias="templateStatus")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
