

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .advanced_auth_auth_flow_type import AdvancedAuthAuthFlowType
from .o_auth_config_specification import OAuthConfigSpecification


class AdvancedAuth(UniversalBaseModel):
    auth_flow_type: typing_extensions.Annotated[
        typing.Optional[AdvancedAuthAuthFlowType], FieldMetadata(alias="authFlowType")
    ] = None
    oauth_config_specification: typing_extensions.Annotated[
        typing.Optional[OAuthConfigSpecification], FieldMetadata(alias="oauthConfigSpecification")
    ] = None
    predicate_key: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="predicateKey")
    ] = pydantic.Field(default=None)
    """
    Json Path to a field in the connectorSpecification that should exist for the advanced auth to be applicable.
    """

    predicate_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="predicateValue")] = (
        pydantic.Field(default=None)
    )
    """
    Value of the predicate_key fields for the advanced auth to be applicable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
