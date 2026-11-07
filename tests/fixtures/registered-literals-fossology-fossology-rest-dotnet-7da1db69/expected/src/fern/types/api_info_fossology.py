

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiInfoFossology(UniversalBaseModel):
    """
    Information about FOSSology server. Values can be null.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version of the FOSSology server
    """

    branch_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="branchName"),
        pydantic.Field(alias="branchName", description="Branch deployed on the FOSSology server"),
    ] = None
    """
    Branch deployed on the FOSSology server
    """

    commit_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="commitHash"),
        pydantic.Field(alias="commitHash", description="Hash of commit deployed on the FOSSology server"),
    ] = None
    """
    Hash of commit deployed on the FOSSology server
    """

    commit_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="commitDate"),
        pydantic.Field(
            alias="commitDate", description="Date of commit deployed on the FOSSology server in\nISO8601 format"
        ),
    ] = None
    """
    Date of commit deployed on the FOSSology server in
    ISO8601 format
    """

    build_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="buildDate"),
        pydantic.Field(alias="buildDate", description="Date on which packages were built in ISO8601 format"),
    ] = None
    """
    Date on which packages were built in ISO8601 format
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
