

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .validate_input_http_definition_headers_item import ValidateInputHttpDefinitionHeadersItem


class ValidateInputHttpDefinition(UniversalBaseModel):
    forward_client_headers: typing.Optional[bool] = None
    headers: typing.Optional[typing.List[ValidateInputHttpDefinitionHeadersItem]] = None
    timeout: typing.Optional[float] = None
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
