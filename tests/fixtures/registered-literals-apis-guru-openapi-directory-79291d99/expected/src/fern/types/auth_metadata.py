

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .auth_supported_methods import AuthSupportedMethods


class AuthMetadata(UniversalBaseModel):
    """
    Metadata that captures information about the Auth features of an institution.
    """

    supported_methods: typing.Optional[AuthSupportedMethods] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
