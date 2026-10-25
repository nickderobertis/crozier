

import typing

from ...types.agent_check_response import AgentCheckResponse
from ...types.agent_close_response import AgentCloseResponse
from ...types.agent_collect_response import AgentCollectResponse
from ...types.agent_final_response import AgentFinalResponse
from ...types.agent_finish_response import AgentFinishResponse
from ...types.agent_join_response import AgentJoinResponse
from ...types.agent_say_response import AgentSayResponse

UseAgentInvitationResponse = typing.Union[
    AgentJoinResponse,
    AgentCheckResponse,
    AgentSayResponse,
    AgentFinishResponse,
    AgentFinalResponse,
    AgentCollectResponse,
    AgentCloseResponse,
]
