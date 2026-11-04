

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InputFileContentParam(UniversalBaseModel):
    """
    A file input to the model.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the file to be sent to the model.
    """

    file_data: typing.Optional[str] = pydantic.Field(default=None)
    """
    The base64-encoded data of the file to be sent to the model.
    """

    file_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the file to be sent to the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
