

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_seventeen_type import BodySeventeenType
from .key_to_multi_value import KeyToMultiValue


class BodySeventeen(UniversalBaseModel):
    """
    parameter body matcher
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    optional: typing.Optional[bool] = None
    type: typing.Optional[BodySeventeenType] = None
    parameters: typing.Optional[KeyToMultiValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
