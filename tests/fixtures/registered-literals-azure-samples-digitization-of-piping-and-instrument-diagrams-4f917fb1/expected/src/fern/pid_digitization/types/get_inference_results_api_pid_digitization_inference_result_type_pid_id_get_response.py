

import typing

from ...types.graph_construction_inference_response import GraphConstructionInferenceResponse
from ...types.line_detection_inference_response import LineDetectionInferenceResponse
from ...types.symbol_detection_inference_response import SymbolDetectionInferenceResponse
from ...types.text_detection_inference_response import TextDetectionInferenceResponse

GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse = typing.Union[
    SymbolDetectionInferenceResponse,
    TextDetectionInferenceResponse,
    LineDetectionInferenceResponse,
    GraphConstructionInferenceResponse,
]
