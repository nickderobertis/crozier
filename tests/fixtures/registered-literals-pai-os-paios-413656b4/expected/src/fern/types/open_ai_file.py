

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_ai_file_object import OpenAiFileObject
from .open_ai_file_purpose import OpenAiFilePurpose
from .open_ai_file_status import OpenAiFileStatus


class OpenAiFile(UniversalBaseModel):
    """
    The `File` object represents a document that has been uploaded to OpenAI.
    """

    id: str = pydantic.Field()
    """
    The file identifier, which can be referenced in the API endpoints.
    """

    bytes: int = pydantic.Field()
    """
    The size of the file, in bytes.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the file was created.
    """

    filename: str = pydantic.Field()
    """
    The name of the file.
    """

    object: OpenAiFileObject = pydantic.Field()
    """
    The object type, which is always `file`.
    """

    purpose: OpenAiFilePurpose = pydantic.Field()
    """
    The intended purpose of the file. Supported values are `fine-tune`, `fine-tune-results`, `assistants`, and `assistants_output`.
    """

    status: OpenAiFileStatus = pydantic.Field()
    """
    Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.
    """

    status_details: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
