



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .all_null_test import AllNullTest
    from .any_of_overlapping import AnyOfOverlapping
    from .any_of_property_holder import AnyOfPropertyHolder
    from .any_of_string_integer import AnyOfStringInteger
    from .cat import Cat
    from .cat_pet_type import CatPetType
    from .create_response import CreateResponse
    from .create_response_base import CreateResponseBase
    from .data_object import DataObject
    from .dedup_test import DedupTest
    from .dedup_test_one import DedupTestOne
    from .dog import Dog
    from .dog_pet_type import DogPetType
    from .input_item import InputItem
    from .input_param import InputParam
    from .model_ids import ModelIds
    from .model_ids_compaction import ModelIdsCompaction
    from .model_ids_responses import ModelIdsResponses
    from .model_ids_responses_one import ModelIdsResponsesOne
    from .model_ids_shared import ModelIdsShared
    from .model_ids_shared_one import ModelIdsSharedOne
    from .nullable_data_object import NullableDataObject
    from .nullable_temperature import NullableTemperature
    from .oas_const_object import OasConstObject
    from .oas_const_object_type import OasConstObjectType
    from .one_of_with_string_overlap import OneOfWithStringOverlap
    from .open_string_model import OpenStringModel
    from .optional_score import OptionalScore
    from .overlapping_object_a import OverlappingObjectA
    from .overlapping_object_b import OverlappingObjectB
    from .parent_with_any_of_overlapping import ParentWithAnyOfOverlapping
    from .pet_by_type import PetByType
    from .ref_holder import RefHolder
    from .response_completed_event import ResponseCompletedEvent
    from .response_created_event import ResponseCreatedEvent
    from .response_stream_event import (
        ResponseStreamEvent,
        ResponseStreamEvent_ResponseCompleted,
        ResponseStreamEvent_ResponseCreated,
    )
    from .single_branch_test import SingleBranchTest
    from .stainless_object import StainlessObject
    from .stainless_object_type import StainlessObjectType
    from .string_enum_model import StringEnumModel
    from .string_overlap_holder import StringOverlapHolder
    from .temperature_container import TemperatureContainer
    from .timestamp_container import TimestampContainer
    from .variant_payload import VariantPayload
_dynamic_imports: typing.Dict[str, str] = {
    "AllNullTest": ".all_null_test",
    "AnyOfOverlapping": ".any_of_overlapping",
    "AnyOfPropertyHolder": ".any_of_property_holder",
    "AnyOfStringInteger": ".any_of_string_integer",
    "Cat": ".cat",
    "CatPetType": ".cat_pet_type",
    "CreateResponse": ".create_response",
    "CreateResponseBase": ".create_response_base",
    "DataObject": ".data_object",
    "DedupTest": ".dedup_test",
    "DedupTestOne": ".dedup_test_one",
    "Dog": ".dog",
    "DogPetType": ".dog_pet_type",
    "InputItem": ".input_item",
    "InputParam": ".input_param",
    "ModelIds": ".model_ids",
    "ModelIdsCompaction": ".model_ids_compaction",
    "ModelIdsResponses": ".model_ids_responses",
    "ModelIdsResponsesOne": ".model_ids_responses_one",
    "ModelIdsShared": ".model_ids_shared",
    "ModelIdsSharedOne": ".model_ids_shared_one",
    "NullableDataObject": ".nullable_data_object",
    "NullableTemperature": ".nullable_temperature",
    "OasConstObject": ".oas_const_object",
    "OasConstObjectType": ".oas_const_object_type",
    "OneOfWithStringOverlap": ".one_of_with_string_overlap",
    "OpenStringModel": ".open_string_model",
    "OptionalScore": ".optional_score",
    "OverlappingObjectA": ".overlapping_object_a",
    "OverlappingObjectB": ".overlapping_object_b",
    "ParentWithAnyOfOverlapping": ".parent_with_any_of_overlapping",
    "PetByType": ".pet_by_type",
    "RefHolder": ".ref_holder",
    "ResponseCompletedEvent": ".response_completed_event",
    "ResponseCreatedEvent": ".response_created_event",
    "ResponseStreamEvent": ".response_stream_event",
    "ResponseStreamEvent_ResponseCompleted": ".response_stream_event",
    "ResponseStreamEvent_ResponseCreated": ".response_stream_event",
    "SingleBranchTest": ".single_branch_test",
    "StainlessObject": ".stainless_object",
    "StainlessObjectType": ".stainless_object_type",
    "StringEnumModel": ".string_enum_model",
    "StringOverlapHolder": ".string_overlap_holder",
    "TemperatureContainer": ".temperature_container",
    "TimestampContainer": ".timestamp_container",
    "VariantPayload": ".variant_payload",
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
    "AllNullTest",
    "AnyOfOverlapping",
    "AnyOfPropertyHolder",
    "AnyOfStringInteger",
    "Cat",
    "CatPetType",
    "CreateResponse",
    "CreateResponseBase",
    "DataObject",
    "DedupTest",
    "DedupTestOne",
    "Dog",
    "DogPetType",
    "InputItem",
    "InputParam",
    "ModelIds",
    "ModelIdsCompaction",
    "ModelIdsResponses",
    "ModelIdsResponsesOne",
    "ModelIdsShared",
    "ModelIdsSharedOne",
    "NullableDataObject",
    "NullableTemperature",
    "OasConstObject",
    "OasConstObjectType",
    "OneOfWithStringOverlap",
    "OpenStringModel",
    "OptionalScore",
    "OverlappingObjectA",
    "OverlappingObjectB",
    "ParentWithAnyOfOverlapping",
    "PetByType",
    "RefHolder",
    "ResponseCompletedEvent",
    "ResponseCreatedEvent",
    "ResponseStreamEvent",
    "ResponseStreamEvent_ResponseCompleted",
    "ResponseStreamEvent_ResponseCreated",
    "SingleBranchTest",
    "StainlessObject",
    "StainlessObjectType",
    "StringEnumModel",
    "StringOverlapHolder",
    "TemperatureContainer",
    "TimestampContainer",
    "VariantPayload",
]
