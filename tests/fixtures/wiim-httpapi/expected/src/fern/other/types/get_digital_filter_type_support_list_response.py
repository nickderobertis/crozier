

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_digital_filter_type_support_list_response_digital_filter_types_item import (
    GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem,
)


class GetDigitalFilterTypeSupportListResponse(UniversalBaseModel):
    digital_filter_types: typing_extensions.Annotated[
        typing.Optional[typing.List[GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem]],
        FieldMetadata(alias="digitalFilterTypes"),
        pydantic.Field(alias="digitalFilterTypes", description="List of supported digital filter types"),
    ] = None
    """
    List of supported digital filter types
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
