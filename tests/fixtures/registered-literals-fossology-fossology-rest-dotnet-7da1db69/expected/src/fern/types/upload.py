

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hash import Hash


class Upload(UniversalBaseModel):
    folderid: typing.Optional[int] = pydantic.Field(default=None)
    """
    The folder id, where the upload is located
    """

    foldername: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the folder where the upload is located
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Upload id of the upload.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the upload.
    """

    uploadname: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name of the upload.
    """

    uploaddate: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date, when the file was uploaded.
    """

    assignee: typing.Optional[int] = pydantic.Field(default=None)
    """
    assignee id of the upload.
    """

    assignee_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="assigneeDate"),
        pydantic.Field(alias="assigneeDate", description="Date, when a user was assigned to the upload."),
    ] = None
    """
    Date, when a user was assigned to the upload.
    """

    closing_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="closingDate"),
        pydantic.Field(alias="closingDate", description="Date, when the upload was closed or rejected."),
    ] = None
    """
    Date, when the upload was closed or rejected.
    """

    hash: typing.Optional[Hash] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
