

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nullable_saved_function_id_id_type import NullableSavedFunctionIdIdType


class NullableSavedFunctionIdId(UniversalBaseModel):
    type: NullableSavedFunctionIdIdType
    id: str
    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
