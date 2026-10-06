



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .align_at import AlignAt
    from .align_shift import AlignShift
    from .alignment import Alignment
    from .cause_exception import CauseException
    from .column_data_set import ColumnDataSet
    from .column_data_set_data_axis import ColumnDataSetDataAxis
    from .column_data_set_rows_item import ColumnDataSetRowsItem
    from .column_header import ColumnHeader
    from .column_index_row_header import ColumnIndexRowHeader
    from .data_axis_option import DataAxisOption
    from .data_set_attributes import DataSetAttributes
    from .data_set_window import DataSetWindow
    from .datum import Datum
    from .delete_response import DeleteResponse
    from .delete_response_embeddings_value import DeleteResponseEmbeddingsValue
    from .delete_response_links_value import DeleteResponseLinksValue
    from .hal_embedding import HalEmbedding
    from .hal_link import HalLink
    from .hal_link_method import HalLinkMethod
    from .hal_link_role import HalLinkRole
    from .header_array_option import HeaderArrayOption
    from .http_validation_error import HttpValidationError
    from .interpolation_method import InterpolationMethod
    from .interpolation_spec import InterpolationSpec
    from .interpolation_spec_value import InterpolationSpecValue
    from .message import Message
    from .message_level import MessageLevel
    from .message_properties import MessageProperties
    from .object_data import ObjectData
    from .object_data_set import ObjectDataSet
    from .queries_list_response import QueriesListResponse
    from .query_execution_message import QueryExecutionMessage
    from .query_execution_message_level import QueryExecutionMessageLevel
    from .query_execution_message_properties import QueryExecutionMessageProperties
    from .query_hal_links import QueryHalLinks
    from .query_input import QueryInput
    from .query_input_aggregation import QueryInputAggregation
    from .query_input_aggregation_three_value_value import QueryInputAggregationThreeValueValue
    from .query_input_aggregation_two_value import QueryInputAggregationTwoValue
    from .query_input_from import QueryInputFrom
    from .query_input_interpolation import QueryInputInterpolation
    from .query_input_interpolation_method import QueryInputInterpolationMethod
    from .query_input_interpolation_method_value import QueryInputInterpolationMethodValue
    from .query_input_interpolation_one import QueryInputInterpolationOne
    from .query_input_interpolation_one_eight import QueryInputInterpolationOneEight
    from .query_input_interpolation_one_eleven import QueryInputInterpolationOneEleven
    from .query_input_interpolation_one_five import QueryInputInterpolationOneFive
    from .query_input_interpolation_one_four import QueryInputInterpolationOneFour
    from .query_input_interpolation_one_nine import QueryInputInterpolationOneNine
    from .query_input_interpolation_one_one import QueryInputInterpolationOneOne
    from .query_input_interpolation_one_seven import QueryInputInterpolationOneSeven
    from .query_input_interpolation_one_six import QueryInputInterpolationOneSix
    from .query_input_interpolation_one_ten import QueryInputInterpolationOneTen
    from .query_input_interpolation_one_thirteen import QueryInputInterpolationOneThirteen
    from .query_input_interpolation_one_three import QueryInputInterpolationOneThree
    from .query_input_interpolation_one_twelve import QueryInputInterpolationOneTwelve
    from .query_input_interpolation_one_two import QueryInputInterpolationOneTwo
    from .query_input_interpolation_one_zero import QueryInputInterpolationOneZero
    from .query_input_until import QueryInputUntil
    from .query_list_hal_links import QueryListHalLinks
    from .query_list_item import QueryListItem
    from .query_output import QueryOutput
    from .query_output_aggregation import QueryOutputAggregation
    from .query_output_aggregation_three_value_value import QueryOutputAggregationThreeValueValue
    from .query_output_aggregation_two_value import QueryOutputAggregationTwoValue
    from .query_output_from import QueryOutputFrom
    from .query_output_interpolation import QueryOutputInterpolation
    from .query_output_interpolation_method import QueryOutputInterpolationMethod
    from .query_output_interpolation_method_value import QueryOutputInterpolationMethodValue
    from .query_output_interpolation_one import QueryOutputInterpolationOne
    from .query_output_interpolation_one_eight import QueryOutputInterpolationOneEight
    from .query_output_interpolation_one_eleven import QueryOutputInterpolationOneEleven
    from .query_output_interpolation_one_five import QueryOutputInterpolationOneFive
    from .query_output_interpolation_one_four import QueryOutputInterpolationOneFour
    from .query_output_interpolation_one_nine import QueryOutputInterpolationOneNine
    from .query_output_interpolation_one_one import QueryOutputInterpolationOneOne
    from .query_output_interpolation_one_seven import QueryOutputInterpolationOneSeven
    from .query_output_interpolation_one_six import QueryOutputInterpolationOneSix
    from .query_output_interpolation_one_ten import QueryOutputInterpolationOneTen
    from .query_output_interpolation_one_thirteen import QueryOutputInterpolationOneThirteen
    from .query_output_interpolation_one_three import QueryOutputInterpolationOneThree
    from .query_output_interpolation_one_twelve import QueryOutputInterpolationOneTwelve
    from .query_output_interpolation_one_two import QueryOutputInterpolationOneTwo
    from .query_output_interpolation_one_zero import QueryOutputInterpolationOneZero
    from .query_output_until import QueryOutputUntil
    from .query_response import QueryResponse
    from .query_result import QueryResult
    from .query_result_data_item import QueryResultDataItem
    from .query_update_input import QueryUpdateInput
    from .render import Render
    from .render_hierarchical import RenderHierarchical
    from .render_mode import RenderMode
    from .role import Role
    from .row_data_set import RowDataSet
    from .row_data_set_columns_item import RowDataSetColumnsItem
    from .row_data_set_data_axis import RowDataSetDataAxis
    from .row_header import RowHeader
    from .row_index_column_header import RowIndexColumnHeader
    from .series_data_set import SeriesDataSet
    from .series_data_set_columns_item import SeriesDataSetColumnsItem
    from .series_data_set_data_axis import SeriesDataSetDataAxis
    from .series_spec import SeriesSpec
    from .series_spec_interpolation import SeriesSpecInterpolation
    from .series_spec_interpolation_method import SeriesSpecInterpolationMethod
    from .series_spec_interpolation_method_value import SeriesSpecInterpolationMethodValue
    from .series_spec_interpolation_one import SeriesSpecInterpolationOne
    from .series_spec_interpolation_one_eight import SeriesSpecInterpolationOneEight
    from .series_spec_interpolation_one_eleven import SeriesSpecInterpolationOneEleven
    from .series_spec_interpolation_one_five import SeriesSpecInterpolationOneFive
    from .series_spec_interpolation_one_four import SeriesSpecInterpolationOneFour
    from .series_spec_interpolation_one_nine import SeriesSpecInterpolationOneNine
    from .series_spec_interpolation_one_one import SeriesSpecInterpolationOneOne
    from .series_spec_interpolation_one_seven import SeriesSpecInterpolationOneSeven
    from .series_spec_interpolation_one_six import SeriesSpecInterpolationOneSix
    from .series_spec_interpolation_one_ten import SeriesSpecInterpolationOneTen
    from .series_spec_interpolation_one_thirteen import SeriesSpecInterpolationOneThirteen
    from .series_spec_interpolation_one_three import SeriesSpecInterpolationOneThree
    from .series_spec_interpolation_one_twelve import SeriesSpecInterpolationOneTwelve
    from .series_spec_interpolation_one_two import SeriesSpecInterpolationOneTwo
    from .series_spec_interpolation_one_zero import SeriesSpecInterpolationOneZero
    from .timestamp import Timestamp
    from .timestamp_iso import TimestampIso
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "AlignAt": ".align_at",
    "AlignShift": ".align_shift",
    "Alignment": ".alignment",
    "CauseException": ".cause_exception",
    "ColumnDataSet": ".column_data_set",
    "ColumnDataSetDataAxis": ".column_data_set_data_axis",
    "ColumnDataSetRowsItem": ".column_data_set_rows_item",
    "ColumnHeader": ".column_header",
    "ColumnIndexRowHeader": ".column_index_row_header",
    "DataAxisOption": ".data_axis_option",
    "DataSetAttributes": ".data_set_attributes",
    "DataSetWindow": ".data_set_window",
    "Datum": ".datum",
    "DeleteResponse": ".delete_response",
    "DeleteResponseEmbeddingsValue": ".delete_response_embeddings_value",
    "DeleteResponseLinksValue": ".delete_response_links_value",
    "HalEmbedding": ".hal_embedding",
    "HalLink": ".hal_link",
    "HalLinkMethod": ".hal_link_method",
    "HalLinkRole": ".hal_link_role",
    "HeaderArrayOption": ".header_array_option",
    "HttpValidationError": ".http_validation_error",
    "InterpolationMethod": ".interpolation_method",
    "InterpolationSpec": ".interpolation_spec",
    "InterpolationSpecValue": ".interpolation_spec_value",
    "Message": ".message",
    "MessageLevel": ".message_level",
    "MessageProperties": ".message_properties",
    "ObjectData": ".object_data",
    "ObjectDataSet": ".object_data_set",
    "QueriesListResponse": ".queries_list_response",
    "QueryExecutionMessage": ".query_execution_message",
    "QueryExecutionMessageLevel": ".query_execution_message_level",
    "QueryExecutionMessageProperties": ".query_execution_message_properties",
    "QueryHalLinks": ".query_hal_links",
    "QueryInput": ".query_input",
    "QueryInputAggregation": ".query_input_aggregation",
    "QueryInputAggregationThreeValueValue": ".query_input_aggregation_three_value_value",
    "QueryInputAggregationTwoValue": ".query_input_aggregation_two_value",
    "QueryInputFrom": ".query_input_from",
    "QueryInputInterpolation": ".query_input_interpolation",
    "QueryInputInterpolationMethod": ".query_input_interpolation_method",
    "QueryInputInterpolationMethodValue": ".query_input_interpolation_method_value",
    "QueryInputInterpolationOne": ".query_input_interpolation_one",
    "QueryInputInterpolationOneEight": ".query_input_interpolation_one_eight",
    "QueryInputInterpolationOneEleven": ".query_input_interpolation_one_eleven",
    "QueryInputInterpolationOneFive": ".query_input_interpolation_one_five",
    "QueryInputInterpolationOneFour": ".query_input_interpolation_one_four",
    "QueryInputInterpolationOneNine": ".query_input_interpolation_one_nine",
    "QueryInputInterpolationOneOne": ".query_input_interpolation_one_one",
    "QueryInputInterpolationOneSeven": ".query_input_interpolation_one_seven",
    "QueryInputInterpolationOneSix": ".query_input_interpolation_one_six",
    "QueryInputInterpolationOneTen": ".query_input_interpolation_one_ten",
    "QueryInputInterpolationOneThirteen": ".query_input_interpolation_one_thirteen",
    "QueryInputInterpolationOneThree": ".query_input_interpolation_one_three",
    "QueryInputInterpolationOneTwelve": ".query_input_interpolation_one_twelve",
    "QueryInputInterpolationOneTwo": ".query_input_interpolation_one_two",
    "QueryInputInterpolationOneZero": ".query_input_interpolation_one_zero",
    "QueryInputUntil": ".query_input_until",
    "QueryListHalLinks": ".query_list_hal_links",
    "QueryListItem": ".query_list_item",
    "QueryOutput": ".query_output",
    "QueryOutputAggregation": ".query_output_aggregation",
    "QueryOutputAggregationThreeValueValue": ".query_output_aggregation_three_value_value",
    "QueryOutputAggregationTwoValue": ".query_output_aggregation_two_value",
    "QueryOutputFrom": ".query_output_from",
    "QueryOutputInterpolation": ".query_output_interpolation",
    "QueryOutputInterpolationMethod": ".query_output_interpolation_method",
    "QueryOutputInterpolationMethodValue": ".query_output_interpolation_method_value",
    "QueryOutputInterpolationOne": ".query_output_interpolation_one",
    "QueryOutputInterpolationOneEight": ".query_output_interpolation_one_eight",
    "QueryOutputInterpolationOneEleven": ".query_output_interpolation_one_eleven",
    "QueryOutputInterpolationOneFive": ".query_output_interpolation_one_five",
    "QueryOutputInterpolationOneFour": ".query_output_interpolation_one_four",
    "QueryOutputInterpolationOneNine": ".query_output_interpolation_one_nine",
    "QueryOutputInterpolationOneOne": ".query_output_interpolation_one_one",
    "QueryOutputInterpolationOneSeven": ".query_output_interpolation_one_seven",
    "QueryOutputInterpolationOneSix": ".query_output_interpolation_one_six",
    "QueryOutputInterpolationOneTen": ".query_output_interpolation_one_ten",
    "QueryOutputInterpolationOneThirteen": ".query_output_interpolation_one_thirteen",
    "QueryOutputInterpolationOneThree": ".query_output_interpolation_one_three",
    "QueryOutputInterpolationOneTwelve": ".query_output_interpolation_one_twelve",
    "QueryOutputInterpolationOneTwo": ".query_output_interpolation_one_two",
    "QueryOutputInterpolationOneZero": ".query_output_interpolation_one_zero",
    "QueryOutputUntil": ".query_output_until",
    "QueryResponse": ".query_response",
    "QueryResult": ".query_result",
    "QueryResultDataItem": ".query_result_data_item",
    "QueryUpdateInput": ".query_update_input",
    "Render": ".render",
    "RenderHierarchical": ".render_hierarchical",
    "RenderMode": ".render_mode",
    "Role": ".role",
    "RowDataSet": ".row_data_set",
    "RowDataSetColumnsItem": ".row_data_set_columns_item",
    "RowDataSetDataAxis": ".row_data_set_data_axis",
    "RowHeader": ".row_header",
    "RowIndexColumnHeader": ".row_index_column_header",
    "SeriesDataSet": ".series_data_set",
    "SeriesDataSetColumnsItem": ".series_data_set_columns_item",
    "SeriesDataSetDataAxis": ".series_data_set_data_axis",
    "SeriesSpec": ".series_spec",
    "SeriesSpecInterpolation": ".series_spec_interpolation",
    "SeriesSpecInterpolationMethod": ".series_spec_interpolation_method",
    "SeriesSpecInterpolationMethodValue": ".series_spec_interpolation_method_value",
    "SeriesSpecInterpolationOne": ".series_spec_interpolation_one",
    "SeriesSpecInterpolationOneEight": ".series_spec_interpolation_one_eight",
    "SeriesSpecInterpolationOneEleven": ".series_spec_interpolation_one_eleven",
    "SeriesSpecInterpolationOneFive": ".series_spec_interpolation_one_five",
    "SeriesSpecInterpolationOneFour": ".series_spec_interpolation_one_four",
    "SeriesSpecInterpolationOneNine": ".series_spec_interpolation_one_nine",
    "SeriesSpecInterpolationOneOne": ".series_spec_interpolation_one_one",
    "SeriesSpecInterpolationOneSeven": ".series_spec_interpolation_one_seven",
    "SeriesSpecInterpolationOneSix": ".series_spec_interpolation_one_six",
    "SeriesSpecInterpolationOneTen": ".series_spec_interpolation_one_ten",
    "SeriesSpecInterpolationOneThirteen": ".series_spec_interpolation_one_thirteen",
    "SeriesSpecInterpolationOneThree": ".series_spec_interpolation_one_three",
    "SeriesSpecInterpolationOneTwelve": ".series_spec_interpolation_one_twelve",
    "SeriesSpecInterpolationOneTwo": ".series_spec_interpolation_one_two",
    "SeriesSpecInterpolationOneZero": ".series_spec_interpolation_one_zero",
    "Timestamp": ".timestamp",
    "TimestampIso": ".timestamp_iso",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "AlignAt",
    "AlignShift",
    "Alignment",
    "CauseException",
    "ColumnDataSet",
    "ColumnDataSetDataAxis",
    "ColumnDataSetRowsItem",
    "ColumnHeader",
    "ColumnIndexRowHeader",
    "DataAxisOption",
    "DataSetAttributes",
    "DataSetWindow",
    "Datum",
    "DeleteResponse",
    "DeleteResponseEmbeddingsValue",
    "DeleteResponseLinksValue",
    "HalEmbedding",
    "HalLink",
    "HalLinkMethod",
    "HalLinkRole",
    "HeaderArrayOption",
    "HttpValidationError",
    "InterpolationMethod",
    "InterpolationSpec",
    "InterpolationSpecValue",
    "Message",
    "MessageLevel",
    "MessageProperties",
    "ObjectData",
    "ObjectDataSet",
    "QueriesListResponse",
    "QueryExecutionMessage",
    "QueryExecutionMessageLevel",
    "QueryExecutionMessageProperties",
    "QueryHalLinks",
    "QueryInput",
    "QueryInputAggregation",
    "QueryInputAggregationThreeValueValue",
    "QueryInputAggregationTwoValue",
    "QueryInputFrom",
    "QueryInputInterpolation",
    "QueryInputInterpolationMethod",
    "QueryInputInterpolationMethodValue",
    "QueryInputInterpolationOne",
    "QueryInputInterpolationOneEight",
    "QueryInputInterpolationOneEleven",
    "QueryInputInterpolationOneFive",
    "QueryInputInterpolationOneFour",
    "QueryInputInterpolationOneNine",
    "QueryInputInterpolationOneOne",
    "QueryInputInterpolationOneSeven",
    "QueryInputInterpolationOneSix",
    "QueryInputInterpolationOneTen",
    "QueryInputInterpolationOneThirteen",
    "QueryInputInterpolationOneThree",
    "QueryInputInterpolationOneTwelve",
    "QueryInputInterpolationOneTwo",
    "QueryInputInterpolationOneZero",
    "QueryInputUntil",
    "QueryListHalLinks",
    "QueryListItem",
    "QueryOutput",
    "QueryOutputAggregation",
    "QueryOutputAggregationThreeValueValue",
    "QueryOutputAggregationTwoValue",
    "QueryOutputFrom",
    "QueryOutputInterpolation",
    "QueryOutputInterpolationMethod",
    "QueryOutputInterpolationMethodValue",
    "QueryOutputInterpolationOne",
    "QueryOutputInterpolationOneEight",
    "QueryOutputInterpolationOneEleven",
    "QueryOutputInterpolationOneFive",
    "QueryOutputInterpolationOneFour",
    "QueryOutputInterpolationOneNine",
    "QueryOutputInterpolationOneOne",
    "QueryOutputInterpolationOneSeven",
    "QueryOutputInterpolationOneSix",
    "QueryOutputInterpolationOneTen",
    "QueryOutputInterpolationOneThirteen",
    "QueryOutputInterpolationOneThree",
    "QueryOutputInterpolationOneTwelve",
    "QueryOutputInterpolationOneTwo",
    "QueryOutputInterpolationOneZero",
    "QueryOutputUntil",
    "QueryResponse",
    "QueryResult",
    "QueryResultDataItem",
    "QueryUpdateInput",
    "Render",
    "RenderHierarchical",
    "RenderMode",
    "Role",
    "RowDataSet",
    "RowDataSetColumnsItem",
    "RowDataSetDataAxis",
    "RowHeader",
    "RowIndexColumnHeader",
    "SeriesDataSet",
    "SeriesDataSetColumnsItem",
    "SeriesDataSetDataAxis",
    "SeriesSpec",
    "SeriesSpecInterpolation",
    "SeriesSpecInterpolationMethod",
    "SeriesSpecInterpolationMethodValue",
    "SeriesSpecInterpolationOne",
    "SeriesSpecInterpolationOneEight",
    "SeriesSpecInterpolationOneEleven",
    "SeriesSpecInterpolationOneFive",
    "SeriesSpecInterpolationOneFour",
    "SeriesSpecInterpolationOneNine",
    "SeriesSpecInterpolationOneOne",
    "SeriesSpecInterpolationOneSeven",
    "SeriesSpecInterpolationOneSix",
    "SeriesSpecInterpolationOneTen",
    "SeriesSpecInterpolationOneThirteen",
    "SeriesSpecInterpolationOneThree",
    "SeriesSpecInterpolationOneTwelve",
    "SeriesSpecInterpolationOneTwo",
    "SeriesSpecInterpolationOneZero",
    "Timestamp",
    "TimestampIso",
    "ValidationError",
    "ValidationErrorLocItem",
]
