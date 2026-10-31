



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .complex_types_any_and_unknown_response import ComplexTypesAnyAndUnknownResponse
    from .complex_types_any_and_unknown_response_result import ComplexTypesAnyAndUnknownResponseResult
    from .complex_types_any_and_unknown_response_result_data import ComplexTypesAnyAndUnknownResponseResultData
    from .complex_types_branded_response import ComplexTypesBrandedResponse
    from .complex_types_branded_response_result import ComplexTypesBrandedResponseResult
    from .complex_types_branded_response_result_data import ComplexTypesBrandedResponseResultData
    from .complex_types_complex_arrays_response import ComplexTypesComplexArraysResponse
    from .complex_types_complex_arrays_response_result import ComplexTypesComplexArraysResponseResult
    from .complex_types_complex_arrays_response_result_data import ComplexTypesComplexArraysResponseResultData
    from .complex_types_complex_arrays_response_result_data_items_item import (
        ComplexTypesComplexArraysResponseResultDataItemsItem,
    )
    from .complex_types_create_content_response import ComplexTypesCreateContentResponse
    from .complex_types_create_content_response_result import ComplexTypesCreateContentResponseResult
    from .complex_types_create_content_response_result_data import (
        ComplexTypesCreateContentResponseResultData,
        ComplexTypesCreateContentResponseResultData_Error,
        ComplexTypesCreateContentResponseResultData_Success,
    )
    from .complex_types_create_content_response_result_data_error import (
        ComplexTypesCreateContentResponseResultDataError,
    )
    from .complex_types_create_content_response_result_data_success import (
        ComplexTypesCreateContentResponseResultDataSuccess,
    )
    from .complex_types_date_type_response import ComplexTypesDateTypeResponse
    from .complex_types_date_type_response_result import ComplexTypesDateTypeResponseResult
    from .complex_types_date_type_response_result_data import ComplexTypesDateTypeResponseResultData
    from .complex_types_deeply_nested_response import ComplexTypesDeeplyNestedResponse
    from .complex_types_deeply_nested_response_result import ComplexTypesDeeplyNestedResponseResult
    from .complex_types_deeply_nested_response_result_data import ComplexTypesDeeplyNestedResponseResultData
    from .complex_types_deeply_nested_response_result_data_level1 import (
        ComplexTypesDeeplyNestedResponseResultDataLevel1,
    )
    from .complex_types_deeply_nested_response_result_data_level1level2 import (
        ComplexTypesDeeplyNestedResponseResultDataLevel1Level2,
    )
    from .complex_types_deeply_nested_response_result_data_level1level2level3 import (
        ComplexTypesDeeplyNestedResponseResultDataLevel1Level2Level3,
    )
    from .complex_types_defaults_response import ComplexTypesDefaultsResponse
    from .complex_types_defaults_response_result import ComplexTypesDefaultsResponseResult
    from .complex_types_defaults_response_result_data import ComplexTypesDefaultsResponseResultData
    from .complex_types_defaults_response_result_data_sort import ComplexTypesDefaultsResponseResultDataSort
    from .complex_types_discriminated_union_request import (
        ComplexTypesDiscriminatedUnionRequest,
        ComplexTypesDiscriminatedUnionRequest_Image,
        ComplexTypesDiscriminatedUnionRequest_Text,
        ComplexTypesDiscriminatedUnionRequest_Video,
    )
    from .complex_types_discriminated_union_request_image import ComplexTypesDiscriminatedUnionRequestImage
    from .complex_types_discriminated_union_request_text import ComplexTypesDiscriminatedUnionRequestText
    from .complex_types_discriminated_union_request_video import ComplexTypesDiscriminatedUnionRequestVideo
    from .complex_types_discriminated_union_response import ComplexTypesDiscriminatedUnionResponse
    from .complex_types_discriminated_union_response_result import ComplexTypesDiscriminatedUnionResponseResult
    from .complex_types_discriminated_union_response_result_data import (
        ComplexTypesDiscriminatedUnionResponseResultData,
        ComplexTypesDiscriminatedUnionResponseResultData_Image,
        ComplexTypesDiscriminatedUnionResponseResultData_Text,
        ComplexTypesDiscriminatedUnionResponseResultData_Video,
    )
    from .complex_types_discriminated_union_response_result_data_image import (
        ComplexTypesDiscriminatedUnionResponseResultDataImage,
    )
    from .complex_types_discriminated_union_response_result_data_text import (
        ComplexTypesDiscriminatedUnionResponseResultDataText,
    )
    from .complex_types_discriminated_union_response_result_data_video import (
        ComplexTypesDiscriminatedUnionResponseResultDataVideo,
    )
    from .complex_types_intersection_response import ComplexTypesIntersectionResponse
    from .complex_types_intersection_response_result import ComplexTypesIntersectionResponseResult
    from .complex_types_intersection_response_result_data import ComplexTypesIntersectionResponseResultData
    from .complex_types_literal_response import ComplexTypesLiteralResponse
    from .complex_types_literal_response_result import ComplexTypesLiteralResponseResult
    from .complex_types_literal_response_result_data import ComplexTypesLiteralResponseResultData
    from .complex_types_literal_response_result_data_str_lit import ComplexTypesLiteralResponseResultDataStrLit
    from .complex_types_literal_union_response import ComplexTypesLiteralUnionResponse
    from .complex_types_literal_union_response_result import ComplexTypesLiteralUnionResponseResult
    from .complex_types_literal_union_response_result_data import ComplexTypesLiteralUnionResponseResultData
    from .complex_types_literal_union_response_result_data_color import ComplexTypesLiteralUnionResponseResultDataColor
    from .complex_types_native_enum_response import ComplexTypesNativeEnumResponse
    from .complex_types_native_enum_response_result import ComplexTypesNativeEnumResponseResult
    from .complex_types_native_enum_response_result_data import ComplexTypesNativeEnumResponseResultData
    from .complex_types_native_enum_response_result_data_direction import (
        ComplexTypesNativeEnumResponseResultDataDirection,
    )
    from .complex_types_nullable_union_response import ComplexTypesNullableUnionResponse
    from .complex_types_nullable_union_response_result import ComplexTypesNullableUnionResponseResult
    from .complex_types_nullable_union_response_result_data import ComplexTypesNullableUnionResponseResultData
    from .complex_types_nullable_union_response_result_data_optional_value import (
        ComplexTypesNullableUnionResponseResultDataOptionalValue,
    )
    from .complex_types_nullable_union_response_result_data_value import (
        ComplexTypesNullableUnionResponseResultDataValue,
    )
    from .complex_types_passthrough_response import ComplexTypesPassthroughResponse
    from .complex_types_passthrough_response_result import ComplexTypesPassthroughResponseResult
    from .complex_types_passthrough_response_result_data import ComplexTypesPassthroughResponseResultData
    from .complex_types_piped_response import ComplexTypesPipedResponse
    from .complex_types_piped_response_result import ComplexTypesPipedResponseResult
    from .complex_types_piped_response_result_data import ComplexTypesPipedResponseResultData
    from .complex_types_record_response import ComplexTypesRecordResponse
    from .complex_types_record_response_result import ComplexTypesRecordResponseResult
    from .complex_types_record_response_result_data import ComplexTypesRecordResponseResultData
    from .complex_types_refined_response import ComplexTypesRefinedResponse
    from .complex_types_refined_response_result import ComplexTypesRefinedResponseResult
    from .complex_types_refined_response_result_data import ComplexTypesRefinedResponseResultData
    from .complex_types_search_response import ComplexTypesSearchResponse
    from .complex_types_search_response_result import ComplexTypesSearchResponseResult
    from .complex_types_search_response_result_data import ComplexTypesSearchResponseResultData
    from .complex_types_search_response_result_data_results_item import ComplexTypesSearchResponseResultDataResultsItem
    from .complex_types_strict_response import ComplexTypesStrictResponse
    from .complex_types_strict_response_result import ComplexTypesStrictResponseResult
    from .complex_types_strict_response_result_data import ComplexTypesStrictResponseResultData
    from .complex_types_tuple_response import ComplexTypesTupleResponse
    from .complex_types_tuple_response_result import ComplexTypesTupleResponseResult
    from .complex_types_tuple_response_result_data import ComplexTypesTupleResponseResultData
    from .complex_types_union_response import ComplexTypesUnionResponse
    from .complex_types_union_response_result import ComplexTypesUnionResponseResult
    from .complex_types_union_response_result_data import ComplexTypesUnionResponseResultData
    from .complex_types_union_response_result_data_value import ComplexTypesUnionResponseResultDataValue
    from .complex_types_with_catch_response import ComplexTypesWithCatchResponse
    from .complex_types_with_catch_response_result import ComplexTypesWithCatchResponseResult
    from .complex_types_with_catch_response_result_data import ComplexTypesWithCatchResponseResultData
    from .complex_types_with_catch_response_result_data_status import ComplexTypesWithCatchResponseResultDataStatus
    from .complex_types_zod_enum_response import ComplexTypesZodEnumResponse
    from .complex_types_zod_enum_response_result import ComplexTypesZodEnumResponseResult
    from .complex_types_zod_enum_response_result_data import ComplexTypesZodEnumResponseResultData
    from .complex_types_zod_enum_response_result_data_status import ComplexTypesZodEnumResponseResultDataStatus
_dynamic_imports: typing.Dict[str, str] = {
    "ComplexTypesAnyAndUnknownResponse": ".complex_types_any_and_unknown_response",
    "ComplexTypesAnyAndUnknownResponseResult": ".complex_types_any_and_unknown_response_result",
    "ComplexTypesAnyAndUnknownResponseResultData": ".complex_types_any_and_unknown_response_result_data",
    "ComplexTypesBrandedResponse": ".complex_types_branded_response",
    "ComplexTypesBrandedResponseResult": ".complex_types_branded_response_result",
    "ComplexTypesBrandedResponseResultData": ".complex_types_branded_response_result_data",
    "ComplexTypesComplexArraysResponse": ".complex_types_complex_arrays_response",
    "ComplexTypesComplexArraysResponseResult": ".complex_types_complex_arrays_response_result",
    "ComplexTypesComplexArraysResponseResultData": ".complex_types_complex_arrays_response_result_data",
    "ComplexTypesComplexArraysResponseResultDataItemsItem": ".complex_types_complex_arrays_response_result_data_items_item",
    "ComplexTypesCreateContentResponse": ".complex_types_create_content_response",
    "ComplexTypesCreateContentResponseResult": ".complex_types_create_content_response_result",
    "ComplexTypesCreateContentResponseResultData": ".complex_types_create_content_response_result_data",
    "ComplexTypesCreateContentResponseResultDataError": ".complex_types_create_content_response_result_data_error",
    "ComplexTypesCreateContentResponseResultDataSuccess": ".complex_types_create_content_response_result_data_success",
    "ComplexTypesCreateContentResponseResultData_Error": ".complex_types_create_content_response_result_data",
    "ComplexTypesCreateContentResponseResultData_Success": ".complex_types_create_content_response_result_data",
    "ComplexTypesDateTypeResponse": ".complex_types_date_type_response",
    "ComplexTypesDateTypeResponseResult": ".complex_types_date_type_response_result",
    "ComplexTypesDateTypeResponseResultData": ".complex_types_date_type_response_result_data",
    "ComplexTypesDeeplyNestedResponse": ".complex_types_deeply_nested_response",
    "ComplexTypesDeeplyNestedResponseResult": ".complex_types_deeply_nested_response_result",
    "ComplexTypesDeeplyNestedResponseResultData": ".complex_types_deeply_nested_response_result_data",
    "ComplexTypesDeeplyNestedResponseResultDataLevel1": ".complex_types_deeply_nested_response_result_data_level1",
    "ComplexTypesDeeplyNestedResponseResultDataLevel1Level2": ".complex_types_deeply_nested_response_result_data_level1level2",
    "ComplexTypesDeeplyNestedResponseResultDataLevel1Level2Level3": ".complex_types_deeply_nested_response_result_data_level1level2level3",
    "ComplexTypesDefaultsResponse": ".complex_types_defaults_response",
    "ComplexTypesDefaultsResponseResult": ".complex_types_defaults_response_result",
    "ComplexTypesDefaultsResponseResultData": ".complex_types_defaults_response_result_data",
    "ComplexTypesDefaultsResponseResultDataSort": ".complex_types_defaults_response_result_data_sort",
    "ComplexTypesDiscriminatedUnionRequest": ".complex_types_discriminated_union_request",
    "ComplexTypesDiscriminatedUnionRequestImage": ".complex_types_discriminated_union_request_image",
    "ComplexTypesDiscriminatedUnionRequestText": ".complex_types_discriminated_union_request_text",
    "ComplexTypesDiscriminatedUnionRequestVideo": ".complex_types_discriminated_union_request_video",
    "ComplexTypesDiscriminatedUnionRequest_Image": ".complex_types_discriminated_union_request",
    "ComplexTypesDiscriminatedUnionRequest_Text": ".complex_types_discriminated_union_request",
    "ComplexTypesDiscriminatedUnionRequest_Video": ".complex_types_discriminated_union_request",
    "ComplexTypesDiscriminatedUnionResponse": ".complex_types_discriminated_union_response",
    "ComplexTypesDiscriminatedUnionResponseResult": ".complex_types_discriminated_union_response_result",
    "ComplexTypesDiscriminatedUnionResponseResultData": ".complex_types_discriminated_union_response_result_data",
    "ComplexTypesDiscriminatedUnionResponseResultDataImage": ".complex_types_discriminated_union_response_result_data_image",
    "ComplexTypesDiscriminatedUnionResponseResultDataText": ".complex_types_discriminated_union_response_result_data_text",
    "ComplexTypesDiscriminatedUnionResponseResultDataVideo": ".complex_types_discriminated_union_response_result_data_video",
    "ComplexTypesDiscriminatedUnionResponseResultData_Image": ".complex_types_discriminated_union_response_result_data",
    "ComplexTypesDiscriminatedUnionResponseResultData_Text": ".complex_types_discriminated_union_response_result_data",
    "ComplexTypesDiscriminatedUnionResponseResultData_Video": ".complex_types_discriminated_union_response_result_data",
    "ComplexTypesIntersectionResponse": ".complex_types_intersection_response",
    "ComplexTypesIntersectionResponseResult": ".complex_types_intersection_response_result",
    "ComplexTypesIntersectionResponseResultData": ".complex_types_intersection_response_result_data",
    "ComplexTypesLiteralResponse": ".complex_types_literal_response",
    "ComplexTypesLiteralResponseResult": ".complex_types_literal_response_result",
    "ComplexTypesLiteralResponseResultData": ".complex_types_literal_response_result_data",
    "ComplexTypesLiteralResponseResultDataStrLit": ".complex_types_literal_response_result_data_str_lit",
    "ComplexTypesLiteralUnionResponse": ".complex_types_literal_union_response",
    "ComplexTypesLiteralUnionResponseResult": ".complex_types_literal_union_response_result",
    "ComplexTypesLiteralUnionResponseResultData": ".complex_types_literal_union_response_result_data",
    "ComplexTypesLiteralUnionResponseResultDataColor": ".complex_types_literal_union_response_result_data_color",
    "ComplexTypesNativeEnumResponse": ".complex_types_native_enum_response",
    "ComplexTypesNativeEnumResponseResult": ".complex_types_native_enum_response_result",
    "ComplexTypesNativeEnumResponseResultData": ".complex_types_native_enum_response_result_data",
    "ComplexTypesNativeEnumResponseResultDataDirection": ".complex_types_native_enum_response_result_data_direction",
    "ComplexTypesNullableUnionResponse": ".complex_types_nullable_union_response",
    "ComplexTypesNullableUnionResponseResult": ".complex_types_nullable_union_response_result",
    "ComplexTypesNullableUnionResponseResultData": ".complex_types_nullable_union_response_result_data",
    "ComplexTypesNullableUnionResponseResultDataOptionalValue": ".complex_types_nullable_union_response_result_data_optional_value",
    "ComplexTypesNullableUnionResponseResultDataValue": ".complex_types_nullable_union_response_result_data_value",
    "ComplexTypesPassthroughResponse": ".complex_types_passthrough_response",
    "ComplexTypesPassthroughResponseResult": ".complex_types_passthrough_response_result",
    "ComplexTypesPassthroughResponseResultData": ".complex_types_passthrough_response_result_data",
    "ComplexTypesPipedResponse": ".complex_types_piped_response",
    "ComplexTypesPipedResponseResult": ".complex_types_piped_response_result",
    "ComplexTypesPipedResponseResultData": ".complex_types_piped_response_result_data",
    "ComplexTypesRecordResponse": ".complex_types_record_response",
    "ComplexTypesRecordResponseResult": ".complex_types_record_response_result",
    "ComplexTypesRecordResponseResultData": ".complex_types_record_response_result_data",
    "ComplexTypesRefinedResponse": ".complex_types_refined_response",
    "ComplexTypesRefinedResponseResult": ".complex_types_refined_response_result",
    "ComplexTypesRefinedResponseResultData": ".complex_types_refined_response_result_data",
    "ComplexTypesSearchResponse": ".complex_types_search_response",
    "ComplexTypesSearchResponseResult": ".complex_types_search_response_result",
    "ComplexTypesSearchResponseResultData": ".complex_types_search_response_result_data",
    "ComplexTypesSearchResponseResultDataResultsItem": ".complex_types_search_response_result_data_results_item",
    "ComplexTypesStrictResponse": ".complex_types_strict_response",
    "ComplexTypesStrictResponseResult": ".complex_types_strict_response_result",
    "ComplexTypesStrictResponseResultData": ".complex_types_strict_response_result_data",
    "ComplexTypesTupleResponse": ".complex_types_tuple_response",
    "ComplexTypesTupleResponseResult": ".complex_types_tuple_response_result",
    "ComplexTypesTupleResponseResultData": ".complex_types_tuple_response_result_data",
    "ComplexTypesUnionResponse": ".complex_types_union_response",
    "ComplexTypesUnionResponseResult": ".complex_types_union_response_result",
    "ComplexTypesUnionResponseResultData": ".complex_types_union_response_result_data",
    "ComplexTypesUnionResponseResultDataValue": ".complex_types_union_response_result_data_value",
    "ComplexTypesWithCatchResponse": ".complex_types_with_catch_response",
    "ComplexTypesWithCatchResponseResult": ".complex_types_with_catch_response_result",
    "ComplexTypesWithCatchResponseResultData": ".complex_types_with_catch_response_result_data",
    "ComplexTypesWithCatchResponseResultDataStatus": ".complex_types_with_catch_response_result_data_status",
    "ComplexTypesZodEnumResponse": ".complex_types_zod_enum_response",
    "ComplexTypesZodEnumResponseResult": ".complex_types_zod_enum_response_result",
    "ComplexTypesZodEnumResponseResultData": ".complex_types_zod_enum_response_result_data",
    "ComplexTypesZodEnumResponseResultDataStatus": ".complex_types_zod_enum_response_result_data_status",
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
    "ComplexTypesAnyAndUnknownResponse",
    "ComplexTypesAnyAndUnknownResponseResult",
    "ComplexTypesAnyAndUnknownResponseResultData",
    "ComplexTypesBrandedResponse",
    "ComplexTypesBrandedResponseResult",
    "ComplexTypesBrandedResponseResultData",
    "ComplexTypesComplexArraysResponse",
    "ComplexTypesComplexArraysResponseResult",
    "ComplexTypesComplexArraysResponseResultData",
    "ComplexTypesComplexArraysResponseResultDataItemsItem",
    "ComplexTypesCreateContentResponse",
    "ComplexTypesCreateContentResponseResult",
    "ComplexTypesCreateContentResponseResultData",
    "ComplexTypesCreateContentResponseResultDataError",
    "ComplexTypesCreateContentResponseResultDataSuccess",
    "ComplexTypesCreateContentResponseResultData_Error",
    "ComplexTypesCreateContentResponseResultData_Success",
    "ComplexTypesDateTypeResponse",
    "ComplexTypesDateTypeResponseResult",
    "ComplexTypesDateTypeResponseResultData",
    "ComplexTypesDeeplyNestedResponse",
    "ComplexTypesDeeplyNestedResponseResult",
    "ComplexTypesDeeplyNestedResponseResultData",
    "ComplexTypesDeeplyNestedResponseResultDataLevel1",
    "ComplexTypesDeeplyNestedResponseResultDataLevel1Level2",
    "ComplexTypesDeeplyNestedResponseResultDataLevel1Level2Level3",
    "ComplexTypesDefaultsResponse",
    "ComplexTypesDefaultsResponseResult",
    "ComplexTypesDefaultsResponseResultData",
    "ComplexTypesDefaultsResponseResultDataSort",
    "ComplexTypesDiscriminatedUnionRequest",
    "ComplexTypesDiscriminatedUnionRequestImage",
    "ComplexTypesDiscriminatedUnionRequestText",
    "ComplexTypesDiscriminatedUnionRequestVideo",
    "ComplexTypesDiscriminatedUnionRequest_Image",
    "ComplexTypesDiscriminatedUnionRequest_Text",
    "ComplexTypesDiscriminatedUnionRequest_Video",
    "ComplexTypesDiscriminatedUnionResponse",
    "ComplexTypesDiscriminatedUnionResponseResult",
    "ComplexTypesDiscriminatedUnionResponseResultData",
    "ComplexTypesDiscriminatedUnionResponseResultDataImage",
    "ComplexTypesDiscriminatedUnionResponseResultDataText",
    "ComplexTypesDiscriminatedUnionResponseResultDataVideo",
    "ComplexTypesDiscriminatedUnionResponseResultData_Image",
    "ComplexTypesDiscriminatedUnionResponseResultData_Text",
    "ComplexTypesDiscriminatedUnionResponseResultData_Video",
    "ComplexTypesIntersectionResponse",
    "ComplexTypesIntersectionResponseResult",
    "ComplexTypesIntersectionResponseResultData",
    "ComplexTypesLiteralResponse",
    "ComplexTypesLiteralResponseResult",
    "ComplexTypesLiteralResponseResultData",
    "ComplexTypesLiteralResponseResultDataStrLit",
    "ComplexTypesLiteralUnionResponse",
    "ComplexTypesLiteralUnionResponseResult",
    "ComplexTypesLiteralUnionResponseResultData",
    "ComplexTypesLiteralUnionResponseResultDataColor",
    "ComplexTypesNativeEnumResponse",
    "ComplexTypesNativeEnumResponseResult",
    "ComplexTypesNativeEnumResponseResultData",
    "ComplexTypesNativeEnumResponseResultDataDirection",
    "ComplexTypesNullableUnionResponse",
    "ComplexTypesNullableUnionResponseResult",
    "ComplexTypesNullableUnionResponseResultData",
    "ComplexTypesNullableUnionResponseResultDataOptionalValue",
    "ComplexTypesNullableUnionResponseResultDataValue",
    "ComplexTypesPassthroughResponse",
    "ComplexTypesPassthroughResponseResult",
    "ComplexTypesPassthroughResponseResultData",
    "ComplexTypesPipedResponse",
    "ComplexTypesPipedResponseResult",
    "ComplexTypesPipedResponseResultData",
    "ComplexTypesRecordResponse",
    "ComplexTypesRecordResponseResult",
    "ComplexTypesRecordResponseResultData",
    "ComplexTypesRefinedResponse",
    "ComplexTypesRefinedResponseResult",
    "ComplexTypesRefinedResponseResultData",
    "ComplexTypesSearchResponse",
    "ComplexTypesSearchResponseResult",
    "ComplexTypesSearchResponseResultData",
    "ComplexTypesSearchResponseResultDataResultsItem",
    "ComplexTypesStrictResponse",
    "ComplexTypesStrictResponseResult",
    "ComplexTypesStrictResponseResultData",
    "ComplexTypesTupleResponse",
    "ComplexTypesTupleResponseResult",
    "ComplexTypesTupleResponseResultData",
    "ComplexTypesUnionResponse",
    "ComplexTypesUnionResponseResult",
    "ComplexTypesUnionResponseResultData",
    "ComplexTypesUnionResponseResultDataValue",
    "ComplexTypesWithCatchResponse",
    "ComplexTypesWithCatchResponseResult",
    "ComplexTypesWithCatchResponseResultData",
    "ComplexTypesWithCatchResponseResultDataStatus",
    "ComplexTypesZodEnumResponse",
    "ComplexTypesZodEnumResponseResult",
    "ComplexTypesZodEnumResponseResultData",
    "ComplexTypesZodEnumResponseResultDataStatus",
]
