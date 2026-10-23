

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostClientWorkspaceIdStorageResponseData(UniversalBaseModel):
    signed_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signedUrl"),
        pydantic.Field(
            alias="signedUrl", description="Presigned POST URL for uploading the file to S3-compatible storage."
        ),
    ] = None
    """
    Presigned POST URL for uploading the file to S3-compatible storage.
    """

    presigned_fields: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="presignedFields"),
        pydantic.Field(
            alias="presignedFields", description="Presigned POST form fields required by S3-compatible storage."
        ),
    ] = None
    """
    Presigned POST form fields required by S3-compatible storage.
    """

    updated_file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedFileName"),
        pydantic.Field(alias="updatedFileName", description="The updated file name after processing."),
    ] = None
    """
    The updated file name after processing.
    """

    file_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileUrl"),
        pydantic.Field(alias="fileUrl", description="URL where the uploaded file can be accessed."),
    ] = None
    """
    URL where the uploaded file can be accessed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
