

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Record(UniversalBaseModel):
    config: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Config"), pydantic.Field(alias="Config")
    ] = None
    construct_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="construct"), pydantic.Field(alias="construct")
    ] = None
    copy_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="copy"), pydantic.Field(alias="copy")
    ] = None
    dict_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dict"), pydantic.Field(alias="dict")
    ] = None
    fields: typing.Optional[str] = None
    from_orm_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="from_orm"), pydantic.Field(alias="from_orm")
    ] = None
    json_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="json"), pydantic.Field(alias="json")
    ] = None
    parse_obj_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parse_obj"), pydantic.Field(alias="parse_obj")
    ] = None
    parse_raw_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parse_raw"), pydantic.Field(alias="parse_raw")
    ] = None
    parse_file_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parse_file"), pydantic.Field(alias="parse_file")
    ] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    schema_json_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schema_json"), pydantic.Field(alias="schema_json")
    ] = None
    validate_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="validate"), pydantic.Field(alias="validate")
    ] = None
    update_forward_refs_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="update_forward_refs"), pydantic.Field(alias="update_forward_refs")
    ] = None
    model_config_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_config"), pydantic.Field(alias="model_config")
    ] = None
    model_fields_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_fields"), pydantic.Field(alias="model_fields")
    ] = None
    model_computed_fields_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="model_computed_fields"),
        pydantic.Field(alias="model_computed_fields"),
    ] = None
    model_extra_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_extra"), pydantic.Field(alias="model_extra")
    ] = None
    model_fields_set_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_fields_set"), pydantic.Field(alias="model_fields_set")
    ] = None
    model_construct_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_construct"), pydantic.Field(alias="model_construct")
    ] = None
    model_copy_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_copy"), pydantic.Field(alias="model_copy")
    ] = None
    model_dump_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_dump"), pydantic.Field(alias="model_dump")
    ] = None
    model_dump_json_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_dump_json"), pydantic.Field(alias="model_dump_json")
    ] = None
    model_json_schema_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_json_schema"), pydantic.Field(alias="model_json_schema")
    ] = None
    model_parametrized_name_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="model_parametrized_name"),
        pydantic.Field(alias="model_parametrized_name"),
    ] = None
    model_post_init_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_post_init"), pydantic.Field(alias="model_post_init")
    ] = None
    model_rebuild_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_rebuild"), pydantic.Field(alias="model_rebuild")
    ] = None
    model_validate_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_validate"), pydantic.Field(alias="model_validate")
    ] = None
    model_validate_json_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="model_validate_json"), pydantic.Field(alias="model_validate_json")
    ] = None
    model_validate_strings_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="model_validate_strings"),
        pydantic.Field(alias="model_validate_strings"),
    ] = None
    self_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="self"), pydantic.Field(alias="self")
    ] = None
    kwargs_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kwargs"), pydantic.Field(alias="kwargs")
    ] = None
    args: typing.Optional[str] = None
    cls: typing.Optional[str] = None
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    list_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="list"), pydantic.Field(alias="list")
    ] = None
    str: typing.Optional[str] = None
    validator: typing.Optional[str] = None
    root_validator: typing.Optional[str] = None
    field: typing.Optional[str] = None
    model: typing.Optional[str] = None
    settings: typing.Optional[str] = None
    register: typing.Optional[str] = None
    update: typing.Optional[str] = None
    keys: typing.Optional[str] = None
    items: typing.Optional[str] = None
    values: typing.Optional[str] = None
    get: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
