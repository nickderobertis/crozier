

import typing

from .batched_facet_data import BatchedFacetData
from .facet_data import FacetData
from .function_data_config import FunctionDataConfig
from .function_data_eight import FunctionDataEight
from .function_data_endpoint import FunctionDataEndpoint
from .function_data_one import FunctionDataOne
from .function_data_schema import FunctionDataSchema
from .function_data_zero import FunctionDataZero
from .graph_data import GraphData

FunctionData = typing.Union[
    FunctionDataZero,
    FunctionDataOne,
    GraphData,
    FunctionDataEndpoint,
    FunctionDataConfig,
    FacetData,
    BatchedFacetData,
    FunctionDataSchema,
    FunctionDataEight,
]
