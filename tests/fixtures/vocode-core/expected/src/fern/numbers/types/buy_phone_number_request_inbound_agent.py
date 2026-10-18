

import typing

from ...types.agent_params import AgentParams
from .buy_phone_number_request_inbound_agent_two import BuyPhoneNumberRequestInboundAgentTwo

BuyPhoneNumberRequestInboundAgent = typing.Union[AgentParams, str, BuyPhoneNumberRequestInboundAgentTwo]
