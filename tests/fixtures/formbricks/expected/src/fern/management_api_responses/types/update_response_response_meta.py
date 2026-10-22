

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_response_response_meta_user_agent import UpdateResponseResponseMetaUserAgent


class UpdateResponseResponseMeta(UniversalBaseModel):
    """
    The meta data of the response
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The source of the response
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the response
    """

    user_agent: typing_extensions.Annotated[
        typing.Optional[UpdateResponseResponseMetaUserAgent],
        FieldMetadata(alias="userAgent"),
        pydantic.Field(alias="userAgent"),
    ] = None
    country: typing.Optional[str] = None
    action: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
