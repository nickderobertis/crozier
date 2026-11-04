

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .triple_nested_map_schema_item_item_value_obj_prop import TripleNestedMapSchemaItemItemValueObjProp


class TripleNestedMapSchemaItemItemValue(UniversalBaseModel):
    string_prop: typing.Optional[str] = pydantic.Field(default=None)
    """
    String inside a map!
    """

    bool_prop: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Bool inside a map!
    """

    ignore_me1: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ignore_me_1"),
        pydantic.Field(alias="ignore_me_1", description="This property will be ignored!"),
    ] = None
    """
    This property will be ignored!
    """

    obj_prop: typing.Optional[TripleNestedMapSchemaItemItemValueObjProp] = pydantic.Field(default=None)
    """
    Object inside a map!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
