



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .inferred_returns_array_of_objects_response import InferredReturnsArrayOfObjectsResponse
    from .inferred_returns_array_of_objects_response_result import InferredReturnsArrayOfObjectsResponseResult
    from .inferred_returns_array_of_objects_response_result_data_item import (
        InferredReturnsArrayOfObjectsResponseResultDataItem,
    )
    from .inferred_returns_bigint_return_response import InferredReturnsBigintReturnResponse
    from .inferred_returns_bigint_return_response_result import InferredReturnsBigintReturnResponseResult
    from .inferred_returns_bigint_return_response_result_data import InferredReturnsBigintReturnResponseResultData
    from .inferred_returns_bool_return_false_response import InferredReturnsBoolReturnFalseResponse
    from .inferred_returns_bool_return_false_response_result import InferredReturnsBoolReturnFalseResponseResult
    from .inferred_returns_bool_return_response import InferredReturnsBoolReturnResponse
    from .inferred_returns_bool_return_response_result import InferredReturnsBoolReturnResponseResult
    from .inferred_returns_bool_return_true_response import InferredReturnsBoolReturnTrueResponse
    from .inferred_returns_bool_return_true_response_result import InferredReturnsBoolReturnTrueResponseResult
    from .inferred_returns_boolean_literal_response import InferredReturnsBooleanLiteralResponse
    from .inferred_returns_boolean_literal_response_result import InferredReturnsBooleanLiteralResponseResult
    from .inferred_returns_branded_returns_response import InferredReturnsBrandedReturnsResponse
    from .inferred_returns_branded_returns_response_result import InferredReturnsBrandedReturnsResponseResult
    from .inferred_returns_branded_returns_response_result_data import InferredReturnsBrandedReturnsResponseResultData
    from .inferred_returns_create_item_response import InferredReturnsCreateItemResponse
    from .inferred_returns_create_item_response_result import InferredReturnsCreateItemResponseResult
    from .inferred_returns_create_item_response_result_data import InferredReturnsCreateItemResponseResultData
    from .inferred_returns_create_item_response_result_data_status import (
        InferredReturnsCreateItemResponseResultDataStatus,
    )
    from .inferred_returns_date_return_response import InferredReturnsDateReturnResponse
    from .inferred_returns_date_return_response_result import InferredReturnsDateReturnResponseResult
    from .inferred_returns_date_return_response_result_data import InferredReturnsDateReturnResponseResultData
    from .inferred_returns_deeply_nested_response import InferredReturnsDeeplyNestedResponse
    from .inferred_returns_deeply_nested_response_result import InferredReturnsDeeplyNestedResponseResult
    from .inferred_returns_deeply_nested_response_result_data import InferredReturnsDeeplyNestedResponseResultData
    from .inferred_returns_deeply_nested_response_result_data_level1 import (
        InferredReturnsDeeplyNestedResponseResultDataLevel1,
    )
    from .inferred_returns_deeply_nested_response_result_data_level1level2 import (
        InferredReturnsDeeplyNestedResponseResultDataLevel1Level2,
    )
    from .inferred_returns_deeply_nested_response_result_data_level1level2level3 import (
        InferredReturnsDeeplyNestedResponseResultDataLevel1Level2Level3,
    )
    from .inferred_returns_discriminated_result_response import InferredReturnsDiscriminatedResultResponse
    from .inferred_returns_discriminated_result_response_result import InferredReturnsDiscriminatedResultResponseResult
    from .inferred_returns_discriminated_result_response_result_data import (
        InferredReturnsDiscriminatedResultResponseResultData,
        InferredReturnsDiscriminatedResultResponseResultData_Error,
        InferredReturnsDiscriminatedResultResponseResultData_Success,
    )
    from .inferred_returns_discriminated_result_response_result_data_error import (
        InferredReturnsDiscriminatedResultResponseResultDataError,
    )
    from .inferred_returns_discriminated_result_response_result_data_success import (
        InferredReturnsDiscriminatedResultResponseResultDataSuccess,
    )
    from .inferred_returns_enum_like_response import InferredReturnsEnumLikeResponse
    from .inferred_returns_enum_like_response_result import InferredReturnsEnumLikeResponseResult
    from .inferred_returns_enum_like_response_result_data import InferredReturnsEnumLikeResponseResultData
    from .inferred_returns_enum_like_response_result_data_status import InferredReturnsEnumLikeResponseResultDataStatus
    from .inferred_returns_literal_array_response import InferredReturnsLiteralArrayResponse
    from .inferred_returns_literal_array_response_result import InferredReturnsLiteralArrayResponseResult
    from .inferred_returns_matrix_response import InferredReturnsMatrixResponse
    from .inferred_returns_matrix_response_result import InferredReturnsMatrixResponseResult
    from .inferred_returns_merged_object_response import InferredReturnsMergedObjectResponse
    from .inferred_returns_merged_object_response_result import InferredReturnsMergedObjectResponseResult
    from .inferred_returns_merged_object_response_result_data import InferredReturnsMergedObjectResponseResultData
    from .inferred_returns_mixed_enum_response import InferredReturnsMixedEnumResponse
    from .inferred_returns_mixed_enum_response_result import InferredReturnsMixedEnumResponseResult
    from .inferred_returns_mixed_enum_response_result_data import InferredReturnsMixedEnumResponseResultData
    from .inferred_returns_mixed_enum_response_result_data_value import InferredReturnsMixedEnumResponseResultDataValue
    from .inferred_returns_mixed_enum_response_result_data_value_two import (
        InferredReturnsMixedEnumResponseResultDataValueTwo,
    )
    from .inferred_returns_mixed_enum_response_result_data_value_zero import (
        InferredReturnsMixedEnumResponseResultDataValueZero,
    )
    from .inferred_returns_mixed_object_response import InferredReturnsMixedObjectResponse
    from .inferred_returns_mixed_object_response_result import InferredReturnsMixedObjectResponseResult
    from .inferred_returns_mixed_object_response_result_data import InferredReturnsMixedObjectResponseResultData
    from .inferred_returns_nested_nullable_response import InferredReturnsNestedNullableResponse
    from .inferred_returns_nested_nullable_response_result import InferredReturnsNestedNullableResponseResult
    from .inferred_returns_nested_nullable_response_result_data import InferredReturnsNestedNullableResponseResultData
    from .inferred_returns_nested_nullable_response_result_data_outer import (
        InferredReturnsNestedNullableResponseResultDataOuter,
    )
    from .inferred_returns_null_return_response import InferredReturnsNullReturnResponse
    from .inferred_returns_null_return_response_result import InferredReturnsNullReturnResponseResult
    from .inferred_returns_nullable_return_response import InferredReturnsNullableReturnResponse
    from .inferred_returns_nullable_return_response_result import InferredReturnsNullableReturnResponseResult
    from .inferred_returns_nullable_return_response_result_data import InferredReturnsNullableReturnResponseResultData
    from .inferred_returns_num_return_response import InferredReturnsNumReturnResponse
    from .inferred_returns_num_return_response_result import InferredReturnsNumReturnResponseResult
    from .inferred_returns_number_literal_response import InferredReturnsNumberLiteralResponse
    from .inferred_returns_number_literal_response_result import InferredReturnsNumberLiteralResponseResult
    from .inferred_returns_numeric_enum_response import InferredReturnsNumericEnumResponse
    from .inferred_returns_numeric_enum_response_result import InferredReturnsNumericEnumResponseResult
    from .inferred_returns_numeric_enum_response_result_data import InferredReturnsNumericEnumResponseResultData
    from .inferred_returns_optional_fields_response import InferredReturnsOptionalFieldsResponse
    from .inferred_returns_optional_fields_response_result import InferredReturnsOptionalFieldsResponseResult
    from .inferred_returns_optional_fields_response_result_data import InferredReturnsOptionalFieldsResponseResultData
    from .inferred_returns_primitive_union_response import InferredReturnsPrimitiveUnionResponse
    from .inferred_returns_primitive_union_response_result import InferredReturnsPrimitiveUnionResponseResult
    from .inferred_returns_primitive_union_response_result_data import InferredReturnsPrimitiveUnionResponseResultData
    from .inferred_returns_primitive_union_response_result_data_value import (
        InferredReturnsPrimitiveUnionResponseResultDataValue,
    )
    from .inferred_returns_record_return_response import InferredReturnsRecordReturnResponse
    from .inferred_returns_record_return_response_result import InferredReturnsRecordReturnResponseResult
    from .inferred_returns_str_return_response import InferredReturnsStrReturnResponse
    from .inferred_returns_str_return_response_result import InferredReturnsStrReturnResponseResult
    from .inferred_returns_string_enum_response import InferredReturnsStringEnumResponse
    from .inferred_returns_string_enum_response_result import InferredReturnsStringEnumResponseResult
    from .inferred_returns_string_enum_response_result_data import InferredReturnsStringEnumResponseResultData
    from .inferred_returns_string_enum_response_result_data_direction import (
        InferredReturnsStringEnumResponseResultDataDirection,
    )
    from .inferred_returns_string_literal_response import InferredReturnsStringLiteralResponse
    from .inferred_returns_string_literal_response_result import InferredReturnsStringLiteralResponseResult
    from .inferred_returns_string_literal_response_result_data import InferredReturnsStringLiteralResponseResultData
    from .inferred_returns_tuple_return_response import InferredReturnsTupleReturnResponse
    from .inferred_returns_tuple_return_response_result import InferredReturnsTupleReturnResponseResult
    from .inferred_returns_void_return_response import InferredReturnsVoidReturnResponse
    from .inferred_returns_void_return_response_result import InferredReturnsVoidReturnResponseResult
_dynamic_imports: typing.Dict[str, str] = {
    "InferredReturnsArrayOfObjectsResponse": ".inferred_returns_array_of_objects_response",
    "InferredReturnsArrayOfObjectsResponseResult": ".inferred_returns_array_of_objects_response_result",
    "InferredReturnsArrayOfObjectsResponseResultDataItem": ".inferred_returns_array_of_objects_response_result_data_item",
    "InferredReturnsBigintReturnResponse": ".inferred_returns_bigint_return_response",
    "InferredReturnsBigintReturnResponseResult": ".inferred_returns_bigint_return_response_result",
    "InferredReturnsBigintReturnResponseResultData": ".inferred_returns_bigint_return_response_result_data",
    "InferredReturnsBoolReturnFalseResponse": ".inferred_returns_bool_return_false_response",
    "InferredReturnsBoolReturnFalseResponseResult": ".inferred_returns_bool_return_false_response_result",
    "InferredReturnsBoolReturnResponse": ".inferred_returns_bool_return_response",
    "InferredReturnsBoolReturnResponseResult": ".inferred_returns_bool_return_response_result",
    "InferredReturnsBoolReturnTrueResponse": ".inferred_returns_bool_return_true_response",
    "InferredReturnsBoolReturnTrueResponseResult": ".inferred_returns_bool_return_true_response_result",
    "InferredReturnsBooleanLiteralResponse": ".inferred_returns_boolean_literal_response",
    "InferredReturnsBooleanLiteralResponseResult": ".inferred_returns_boolean_literal_response_result",
    "InferredReturnsBrandedReturnsResponse": ".inferred_returns_branded_returns_response",
    "InferredReturnsBrandedReturnsResponseResult": ".inferred_returns_branded_returns_response_result",
    "InferredReturnsBrandedReturnsResponseResultData": ".inferred_returns_branded_returns_response_result_data",
    "InferredReturnsCreateItemResponse": ".inferred_returns_create_item_response",
    "InferredReturnsCreateItemResponseResult": ".inferred_returns_create_item_response_result",
    "InferredReturnsCreateItemResponseResultData": ".inferred_returns_create_item_response_result_data",
    "InferredReturnsCreateItemResponseResultDataStatus": ".inferred_returns_create_item_response_result_data_status",
    "InferredReturnsDateReturnResponse": ".inferred_returns_date_return_response",
    "InferredReturnsDateReturnResponseResult": ".inferred_returns_date_return_response_result",
    "InferredReturnsDateReturnResponseResultData": ".inferred_returns_date_return_response_result_data",
    "InferredReturnsDeeplyNestedResponse": ".inferred_returns_deeply_nested_response",
    "InferredReturnsDeeplyNestedResponseResult": ".inferred_returns_deeply_nested_response_result",
    "InferredReturnsDeeplyNestedResponseResultData": ".inferred_returns_deeply_nested_response_result_data",
    "InferredReturnsDeeplyNestedResponseResultDataLevel1": ".inferred_returns_deeply_nested_response_result_data_level1",
    "InferredReturnsDeeplyNestedResponseResultDataLevel1Level2": ".inferred_returns_deeply_nested_response_result_data_level1level2",
    "InferredReturnsDeeplyNestedResponseResultDataLevel1Level2Level3": ".inferred_returns_deeply_nested_response_result_data_level1level2level3",
    "InferredReturnsDiscriminatedResultResponse": ".inferred_returns_discriminated_result_response",
    "InferredReturnsDiscriminatedResultResponseResult": ".inferred_returns_discriminated_result_response_result",
    "InferredReturnsDiscriminatedResultResponseResultData": ".inferred_returns_discriminated_result_response_result_data",
    "InferredReturnsDiscriminatedResultResponseResultDataError": ".inferred_returns_discriminated_result_response_result_data_error",
    "InferredReturnsDiscriminatedResultResponseResultDataSuccess": ".inferred_returns_discriminated_result_response_result_data_success",
    "InferredReturnsDiscriminatedResultResponseResultData_Error": ".inferred_returns_discriminated_result_response_result_data",
    "InferredReturnsDiscriminatedResultResponseResultData_Success": ".inferred_returns_discriminated_result_response_result_data",
    "InferredReturnsEnumLikeResponse": ".inferred_returns_enum_like_response",
    "InferredReturnsEnumLikeResponseResult": ".inferred_returns_enum_like_response_result",
    "InferredReturnsEnumLikeResponseResultData": ".inferred_returns_enum_like_response_result_data",
    "InferredReturnsEnumLikeResponseResultDataStatus": ".inferred_returns_enum_like_response_result_data_status",
    "InferredReturnsLiteralArrayResponse": ".inferred_returns_literal_array_response",
    "InferredReturnsLiteralArrayResponseResult": ".inferred_returns_literal_array_response_result",
    "InferredReturnsMatrixResponse": ".inferred_returns_matrix_response",
    "InferredReturnsMatrixResponseResult": ".inferred_returns_matrix_response_result",
    "InferredReturnsMergedObjectResponse": ".inferred_returns_merged_object_response",
    "InferredReturnsMergedObjectResponseResult": ".inferred_returns_merged_object_response_result",
    "InferredReturnsMergedObjectResponseResultData": ".inferred_returns_merged_object_response_result_data",
    "InferredReturnsMixedEnumResponse": ".inferred_returns_mixed_enum_response",
    "InferredReturnsMixedEnumResponseResult": ".inferred_returns_mixed_enum_response_result",
    "InferredReturnsMixedEnumResponseResultData": ".inferred_returns_mixed_enum_response_result_data",
    "InferredReturnsMixedEnumResponseResultDataValue": ".inferred_returns_mixed_enum_response_result_data_value",
    "InferredReturnsMixedEnumResponseResultDataValueTwo": ".inferred_returns_mixed_enum_response_result_data_value_two",
    "InferredReturnsMixedEnumResponseResultDataValueZero": ".inferred_returns_mixed_enum_response_result_data_value_zero",
    "InferredReturnsMixedObjectResponse": ".inferred_returns_mixed_object_response",
    "InferredReturnsMixedObjectResponseResult": ".inferred_returns_mixed_object_response_result",
    "InferredReturnsMixedObjectResponseResultData": ".inferred_returns_mixed_object_response_result_data",
    "InferredReturnsNestedNullableResponse": ".inferred_returns_nested_nullable_response",
    "InferredReturnsNestedNullableResponseResult": ".inferred_returns_nested_nullable_response_result",
    "InferredReturnsNestedNullableResponseResultData": ".inferred_returns_nested_nullable_response_result_data",
    "InferredReturnsNestedNullableResponseResultDataOuter": ".inferred_returns_nested_nullable_response_result_data_outer",
    "InferredReturnsNullReturnResponse": ".inferred_returns_null_return_response",
    "InferredReturnsNullReturnResponseResult": ".inferred_returns_null_return_response_result",
    "InferredReturnsNullableReturnResponse": ".inferred_returns_nullable_return_response",
    "InferredReturnsNullableReturnResponseResult": ".inferred_returns_nullable_return_response_result",
    "InferredReturnsNullableReturnResponseResultData": ".inferred_returns_nullable_return_response_result_data",
    "InferredReturnsNumReturnResponse": ".inferred_returns_num_return_response",
    "InferredReturnsNumReturnResponseResult": ".inferred_returns_num_return_response_result",
    "InferredReturnsNumberLiteralResponse": ".inferred_returns_number_literal_response",
    "InferredReturnsNumberLiteralResponseResult": ".inferred_returns_number_literal_response_result",
    "InferredReturnsNumericEnumResponse": ".inferred_returns_numeric_enum_response",
    "InferredReturnsNumericEnumResponseResult": ".inferred_returns_numeric_enum_response_result",
    "InferredReturnsNumericEnumResponseResultData": ".inferred_returns_numeric_enum_response_result_data",
    "InferredReturnsOptionalFieldsResponse": ".inferred_returns_optional_fields_response",
    "InferredReturnsOptionalFieldsResponseResult": ".inferred_returns_optional_fields_response_result",
    "InferredReturnsOptionalFieldsResponseResultData": ".inferred_returns_optional_fields_response_result_data",
    "InferredReturnsPrimitiveUnionResponse": ".inferred_returns_primitive_union_response",
    "InferredReturnsPrimitiveUnionResponseResult": ".inferred_returns_primitive_union_response_result",
    "InferredReturnsPrimitiveUnionResponseResultData": ".inferred_returns_primitive_union_response_result_data",
    "InferredReturnsPrimitiveUnionResponseResultDataValue": ".inferred_returns_primitive_union_response_result_data_value",
    "InferredReturnsRecordReturnResponse": ".inferred_returns_record_return_response",
    "InferredReturnsRecordReturnResponseResult": ".inferred_returns_record_return_response_result",
    "InferredReturnsStrReturnResponse": ".inferred_returns_str_return_response",
    "InferredReturnsStrReturnResponseResult": ".inferred_returns_str_return_response_result",
    "InferredReturnsStringEnumResponse": ".inferred_returns_string_enum_response",
    "InferredReturnsStringEnumResponseResult": ".inferred_returns_string_enum_response_result",
    "InferredReturnsStringEnumResponseResultData": ".inferred_returns_string_enum_response_result_data",
    "InferredReturnsStringEnumResponseResultDataDirection": ".inferred_returns_string_enum_response_result_data_direction",
    "InferredReturnsStringLiteralResponse": ".inferred_returns_string_literal_response",
    "InferredReturnsStringLiteralResponseResult": ".inferred_returns_string_literal_response_result",
    "InferredReturnsStringLiteralResponseResultData": ".inferred_returns_string_literal_response_result_data",
    "InferredReturnsTupleReturnResponse": ".inferred_returns_tuple_return_response",
    "InferredReturnsTupleReturnResponseResult": ".inferred_returns_tuple_return_response_result",
    "InferredReturnsVoidReturnResponse": ".inferred_returns_void_return_response",
    "InferredReturnsVoidReturnResponseResult": ".inferred_returns_void_return_response_result",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "InferredReturnsArrayOfObjectsResponse",
    "InferredReturnsArrayOfObjectsResponseResult",
    "InferredReturnsArrayOfObjectsResponseResultDataItem",
    "InferredReturnsBigintReturnResponse",
    "InferredReturnsBigintReturnResponseResult",
    "InferredReturnsBigintReturnResponseResultData",
    "InferredReturnsBoolReturnFalseResponse",
    "InferredReturnsBoolReturnFalseResponseResult",
    "InferredReturnsBoolReturnResponse",
    "InferredReturnsBoolReturnResponseResult",
    "InferredReturnsBoolReturnTrueResponse",
    "InferredReturnsBoolReturnTrueResponseResult",
    "InferredReturnsBooleanLiteralResponse",
    "InferredReturnsBooleanLiteralResponseResult",
    "InferredReturnsBrandedReturnsResponse",
    "InferredReturnsBrandedReturnsResponseResult",
    "InferredReturnsBrandedReturnsResponseResultData",
    "InferredReturnsCreateItemResponse",
    "InferredReturnsCreateItemResponseResult",
    "InferredReturnsCreateItemResponseResultData",
    "InferredReturnsCreateItemResponseResultDataStatus",
    "InferredReturnsDateReturnResponse",
    "InferredReturnsDateReturnResponseResult",
    "InferredReturnsDateReturnResponseResultData",
    "InferredReturnsDeeplyNestedResponse",
    "InferredReturnsDeeplyNestedResponseResult",
    "InferredReturnsDeeplyNestedResponseResultData",
    "InferredReturnsDeeplyNestedResponseResultDataLevel1",
    "InferredReturnsDeeplyNestedResponseResultDataLevel1Level2",
    "InferredReturnsDeeplyNestedResponseResultDataLevel1Level2Level3",
    "InferredReturnsDiscriminatedResultResponse",
    "InferredReturnsDiscriminatedResultResponseResult",
    "InferredReturnsDiscriminatedResultResponseResultData",
    "InferredReturnsDiscriminatedResultResponseResultDataError",
    "InferredReturnsDiscriminatedResultResponseResultDataSuccess",
    "InferredReturnsDiscriminatedResultResponseResultData_Error",
    "InferredReturnsDiscriminatedResultResponseResultData_Success",
    "InferredReturnsEnumLikeResponse",
    "InferredReturnsEnumLikeResponseResult",
    "InferredReturnsEnumLikeResponseResultData",
    "InferredReturnsEnumLikeResponseResultDataStatus",
    "InferredReturnsLiteralArrayResponse",
    "InferredReturnsLiteralArrayResponseResult",
    "InferredReturnsMatrixResponse",
    "InferredReturnsMatrixResponseResult",
    "InferredReturnsMergedObjectResponse",
    "InferredReturnsMergedObjectResponseResult",
    "InferredReturnsMergedObjectResponseResultData",
    "InferredReturnsMixedEnumResponse",
    "InferredReturnsMixedEnumResponseResult",
    "InferredReturnsMixedEnumResponseResultData",
    "InferredReturnsMixedEnumResponseResultDataValue",
    "InferredReturnsMixedEnumResponseResultDataValueTwo",
    "InferredReturnsMixedEnumResponseResultDataValueZero",
    "InferredReturnsMixedObjectResponse",
    "InferredReturnsMixedObjectResponseResult",
    "InferredReturnsMixedObjectResponseResultData",
    "InferredReturnsNestedNullableResponse",
    "InferredReturnsNestedNullableResponseResult",
    "InferredReturnsNestedNullableResponseResultData",
    "InferredReturnsNestedNullableResponseResultDataOuter",
    "InferredReturnsNullReturnResponse",
    "InferredReturnsNullReturnResponseResult",
    "InferredReturnsNullableReturnResponse",
    "InferredReturnsNullableReturnResponseResult",
    "InferredReturnsNullableReturnResponseResultData",
    "InferredReturnsNumReturnResponse",
    "InferredReturnsNumReturnResponseResult",
    "InferredReturnsNumberLiteralResponse",
    "InferredReturnsNumberLiteralResponseResult",
    "InferredReturnsNumericEnumResponse",
    "InferredReturnsNumericEnumResponseResult",
    "InferredReturnsNumericEnumResponseResultData",
    "InferredReturnsOptionalFieldsResponse",
    "InferredReturnsOptionalFieldsResponseResult",
    "InferredReturnsOptionalFieldsResponseResultData",
    "InferredReturnsPrimitiveUnionResponse",
    "InferredReturnsPrimitiveUnionResponseResult",
    "InferredReturnsPrimitiveUnionResponseResultData",
    "InferredReturnsPrimitiveUnionResponseResultDataValue",
    "InferredReturnsRecordReturnResponse",
    "InferredReturnsRecordReturnResponseResult",
    "InferredReturnsStrReturnResponse",
    "InferredReturnsStrReturnResponseResult",
    "InferredReturnsStringEnumResponse",
    "InferredReturnsStringEnumResponseResult",
    "InferredReturnsStringEnumResponseResultData",
    "InferredReturnsStringEnumResponseResultDataDirection",
    "InferredReturnsStringLiteralResponse",
    "InferredReturnsStringLiteralResponseResult",
    "InferredReturnsStringLiteralResponseResultData",
    "InferredReturnsTupleReturnResponse",
    "InferredReturnsTupleReturnResponseResult",
    "InferredReturnsVoidReturnResponse",
    "InferredReturnsVoidReturnResponseResult",
]
