

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .types_object_with_required_field import TypesObjectWithRequiredField


class EndpointsPaginatedResponse(UniversalBaseModel):
    items: typing.List[TypesObjectWithRequiredField]
    next: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
