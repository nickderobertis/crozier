

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_status import ProjectStatus


class Project(UniversalBaseModel):
    id: str
    status: typing.Optional[ProjectStatus] = None
    taxonomy_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="taxonomyName"), pydantic.Field(alias="taxonomyName")
    ]
    branch_name: typing_extensions.Annotated[str, FieldMetadata(alias="branchName"), pydantic.Field(alias="branchName")]
    description: str
    owner_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerName"), pydantic.Field(alias="ownerName")
    ] = None
    is_from_github: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isFromGithub"), pydantic.Field(alias="isFromGithub")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    errors_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="errorsCount"), pydantic.Field(alias="errorsCount")
    ] = None
    github_checkout_commit_sha: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="githubCheckoutCommitSha"),
        pydantic.Field(alias="githubCheckoutCommitSha"),
    ] = None
    github_file_latest_sha: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="githubFileLatestSha"), pydantic.Field(alias="githubFileLatestSha")
    ] = None
    github_pr_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="githubPrUrl"), pydantic.Field(alias="githubPrUrl")
    ] = None
    original_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="originalText"), pydantic.Field(alias="originalText")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
