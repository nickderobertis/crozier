

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay
from .http_forward_validate_action_scheme import HttpForwardValidateActionScheme
from .http_forward_validate_action_validation_mode import HttpForwardValidateActionValidationMode


class HttpForwardValidateAction(UniversalBaseModel):
    """
    forward and validate against an OpenAPI spec
    """

    delay: typing.Optional[Delay] = None
    spec_url_or_payload: typing_extensions.Annotated[
        str, FieldMetadata(alias="specUrlOrPayload"), pydantic.Field(alias="specUrlOrPayload")
    ]
    host: str
    port: typing.Optional[int] = None
    scheme: typing.Optional[HttpForwardValidateActionScheme] = None
    validate_request: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="validateRequest"), pydantic.Field(alias="validateRequest")
    ] = None
    validate_response: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="validateResponse"), pydantic.Field(alias="validateResponse")
    ] = None
    validation_mode: typing_extensions.Annotated[
        typing.Optional[HttpForwardValidateActionValidationMode],
        FieldMetadata(alias="validationMode"),
        pydantic.Field(alias="validationMode"),
    ] = None
    primary: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
