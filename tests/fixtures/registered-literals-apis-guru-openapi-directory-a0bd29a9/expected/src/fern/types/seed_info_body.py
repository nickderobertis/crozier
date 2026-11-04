

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .git_config_options_body import GitConfigOptionsBody
from .repository_info_body import RepositoryInfoBody


class SeedInfoBody(UniversalBaseModel):
    clone_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cloneUrl"), pydantic.Field(alias="cloneUrl")
    ] = None
    git_config: typing_extensions.Annotated[
        typing.Optional[GitConfigOptionsBody], FieldMetadata(alias="gitConfig"), pydantic.Field(alias="gitConfig")
    ] = None
    recurse_clone: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="recurseClone"), pydantic.Field(alias="recurseClone")
    ] = None
    repository: typing.Optional[RepositoryInfoBody] = None
    seed_moniker: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="seedMoniker"), pydantic.Field(alias="seedMoniker")
    ] = None
    seed_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="seedType"), pydantic.Field(alias="seedType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
