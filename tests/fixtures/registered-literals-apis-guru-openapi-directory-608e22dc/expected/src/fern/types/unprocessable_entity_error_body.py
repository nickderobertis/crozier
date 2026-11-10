

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .unprocessable_entity_error_body_invalid_parameters_item import UnprocessableEntityErrorBodyInvalidParametersItem


class UnprocessableEntityErrorBody(UniversalBaseModel):
    detail: str
    instance: str
    invalid_parameters: typing.List[UnprocessableEntityErrorBodyInvalidParametersItem]
    title: str
    type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
