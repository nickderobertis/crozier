

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .azure_location import AzureLocation


class PrebuildReadinessResult(UniversalBaseModel):
    branch_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="branchName"), pydantic.Field(alias="branchName")
    ] = None
    dev_container_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="devContainerPath"), pydantic.Field(alias="devContainerPath")
    ] = None
    location: typing.Optional[AzureLocation] = None
    pool_skus: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="poolSkus"), pydantic.Field(alias="poolSkus")
    ] = None
    prebuild_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="prebuildHash"), pydantic.Field(alias="prebuildHash")
    ] = None
    repo_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="repoId"), pydantic.Field(alias="repoId")
    ] = None
    supported_skus: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="supportedSkus"), pydantic.Field(alias="supportedSkus")
    ] = None
    template_skus: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="templateSkus"), pydantic.Field(alias="templateSkus")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
