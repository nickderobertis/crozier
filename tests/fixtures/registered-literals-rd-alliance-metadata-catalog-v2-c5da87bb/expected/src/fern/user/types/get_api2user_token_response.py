

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetApi2UserTokenResponse(UniversalBaseModel):
    api_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion")
    ] = None
    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Authorization token valid for 600 seconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
