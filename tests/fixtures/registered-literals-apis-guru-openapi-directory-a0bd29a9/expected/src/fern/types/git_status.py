

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GitStatus(UniversalBaseModel):
    ahead: typing.Optional[int] = None
    behind: typing.Optional[int] = None
    branch: typing.Optional[str] = None
    commit: typing.Optional[str] = None
    has_uncommitted_changes: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasUncommittedChanges"),
        pydantic.Field(alias="hasUncommittedChanges"),
    ] = None
    has_unpushed_changes: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasUnpushedChanges"), pydantic.Field(alias="hasUnpushedChanges")
    ] = None
    no_git_repo: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="noGitRepo"), pydantic.Field(alias="noGitRepo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
