

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .auth_specification_auth_type import AuthSpecificationAuthType
from .o_auth2specification import OAuth2Specification


class AuthSpecification(UniversalBaseModel):
    auth_type: typing.Optional[AuthSpecificationAuthType] = None
    oauth2specification: typing_extensions.Annotated[
        typing.Optional[OAuth2Specification], FieldMetadata(alias="oauth2Specification")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
