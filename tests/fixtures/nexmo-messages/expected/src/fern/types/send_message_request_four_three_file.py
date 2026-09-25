

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendMessageRequestFourThreeFile(UniversalBaseModel):
    """
    An object containing details of the file to be sent. Note: allowed file types are `.doc,` `.docx`, `.rtf`, `.dot`, `.dotx`, `.odt`, `.odf`, `.fodt`, `.txt`, `.info`, `.pdf`, `.xps`, `.pdax`, `.eps`, `.xls`, `.xlsx`, `.ods`, `.fods`, `.csv`, `.xlsm`, `.xltx`. Maximum file size is 200MB
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name and extension of the file.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the file attachment *or* the path for the location of the file attachement. If `name` is included, can just be the path. If  `name` is not included, must include the filename and extension.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
