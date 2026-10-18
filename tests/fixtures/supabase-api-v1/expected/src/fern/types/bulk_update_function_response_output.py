

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bulk_update_function_response_output_functions_item import BulkUpdateFunctionResponseOutputFunctionsItem


class BulkUpdateFunctionResponseOutput(UniversalBaseModel):
    functions: typing.List[BulkUpdateFunctionResponseOutputFunctionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
