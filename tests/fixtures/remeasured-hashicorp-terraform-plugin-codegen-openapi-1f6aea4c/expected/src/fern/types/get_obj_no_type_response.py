

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_obj_no_type_response_nested_obj import GetObjNoTypeResponseNestedObj


class GetObjNoTypeResponse(UniversalBaseModel):
    string_prop: typing.Optional[str] = pydantic.Field(default=None)
    """
    String inside an object!
    """

    nested_obj: typing.Optional[GetObjNoTypeResponseNestedObj] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
