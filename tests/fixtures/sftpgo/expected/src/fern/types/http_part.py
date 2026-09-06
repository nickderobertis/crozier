

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .key_value import KeyValue


class HttpPart(UniversalBaseModel):
    name: typing.Optional[str] = None
    headers: typing.Optional[typing.List[KeyValue]] = pydantic.Field(default=None)
    """
    Additional headers. Content-Disposition header is automatically set. Content-Type header is automatically detect for files to attach
    """

    filepath: typing.Optional[str] = pydantic.Field(default=None)
    """
    path to the file to be sent as an attachment
    """

    body: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
