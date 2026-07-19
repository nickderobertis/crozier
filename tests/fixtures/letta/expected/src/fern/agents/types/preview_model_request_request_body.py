

import typing

from ...types.letta_request import LettaRequest
from ...types.letta_streaming_request import LettaStreamingRequest

PreviewModelRequestRequestBody = typing.Union[LettaRequest, LettaStreamingRequest]
