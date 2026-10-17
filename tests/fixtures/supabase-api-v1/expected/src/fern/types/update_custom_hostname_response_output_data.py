

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .update_custom_hostname_response_output_data_result import UpdateCustomHostnameResponseOutputDataResult


class UpdateCustomHostnameResponseOutputData(UniversalBaseModel):
    success: bool
    errors: typing.List["JsonValueOutput"]
    messages: typing.List["JsonValueOutput"]
    result: UpdateCustomHostnameResponseOutputDataResult

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_value_output import JsonValueOutput

update_forward_refs(UpdateCustomHostnameResponseOutputData, JsonValueOutput=JsonValueOutput)
