

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OperatorDbt(UniversalBaseModel):
    dbt_arguments: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="dbtArguments")] = None
    docker_image: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="dockerImage")] = None
    git_repo_branch: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="gitRepoBranch")] = None
    git_repo_url: typing_extensions.Annotated[str, FieldMetadata(alias="gitRepoUrl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
