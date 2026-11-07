

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .http_request_block_parameters_item import HttpRequestBlockParametersItem
from .output_parameter import OutputParameter


class HttpRequestBlock(UniversalBaseModel):
    label: str
    output_parameter: OutputParameter
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    method: typing.Optional[str] = None
    url: typing.Optional[str] = None
    headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    body: typing.Optional[typing.Dict[str, typing.Any]] = None
    timeout: typing.Optional[int] = None
    follow_redirects: typing.Optional[bool] = None
    parameters: typing.Optional[typing.List[HttpRequestBlockParametersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(HttpRequestBlock)
