

import typing

from .batched_facet_data import BatchedFacetData
from .facet_data import FacetData
from .function_data_nullish_config import FunctionDataNullishConfig
from .function_data_nullish_eight import FunctionDataNullishEight
from .function_data_nullish_endpoint import FunctionDataNullishEndpoint
from .function_data_nullish_one import FunctionDataNullishOne
from .function_data_nullish_schema import FunctionDataNullishSchema
from .function_data_nullish_zero import FunctionDataNullishZero
from .graph_data import GraphData

FunctionDataNullish = typing.Union[
    FunctionDataNullishZero,
    FunctionDataNullishOne,
    GraphData,
    FunctionDataNullishEndpoint,
    FunctionDataNullishConfig,
    FacetData,
    BatchedFacetData,
    FunctionDataNullishSchema,
    FunctionDataNullishEight,
]
