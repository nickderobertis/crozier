

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vcs_upload_vcs_type import VcsUploadVcsType


class VcsUpload(UniversalBaseModel):
    """
    To create an upload from a version control system
    """

    vcs_type: typing_extensions.Annotated[
        VcsUploadVcsType, FieldMetadata(alias="vcsType"), pydantic.Field(alias="vcsType", description="VCS type")
    ]
    """
    VCS type
    """

    vcs_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="vcsUrl"), pydantic.Field(alias="vcsUrl", description="URL of the repository")
    ]
    """
    URL of the repository
    """

    vcs_branch: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vcsBranch"),
        pydantic.Field(alias="vcsBranch", description="Branch to checkout for analysis (for Git only)"),
    ] = None
    """
    Branch to checkout for analysis (for Git only)
    """

    vcs_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vcsName"),
        pydantic.Field(alias="vcsName", description="Display name of the upload"),
    ] = None
    """
    Display name of the upload
    """

    vcs_username: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vcsUsername"),
        pydantic.Field(alias="vcsUsername", description="Username for the VCS"),
    ] = None
    """
    Username for the VCS
    """

    vcs_password: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vcsPassword"),
        pydantic.Field(alias="vcsPassword", description="Password for the VCS"),
    ] = None
    """
    Password for the VCS
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
