

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateUploadBodyDirectPut(UniversalBaseModel):
    """
    A transport in which the client writes the whole object through one presigned request.
    """

    size_bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    An advisory byte length, which the server uses to check the provider's size limit early.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
