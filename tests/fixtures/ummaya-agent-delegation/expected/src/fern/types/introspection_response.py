

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .introspection_response_aal_asserted import IntrospectionResponseAalAsserted


class IntrospectionResponse(UniversalBaseModel):
    """
    RFC 7662 shape.
    """

    active: bool
    scope: typing.Optional[str] = None
    exp: typing.Optional[int] = None
    iss: typing.Optional[str] = None
    aud: typing.Optional[str] = None
    aal_asserted: typing.Optional[IntrospectionResponseAalAsserted] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
