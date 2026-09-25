

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AapMessage(UniversalBaseModel):
    """
    Abstract base shape for every typed Auto Agent Protocol payload that travels inside an A2A DataPart. Concrete request and response schemas restrict 'type' to a constant skill-id-shaped value (e.g. inventory.search.request, lead.appointment.response). The AAP version is announced once via the agent-card extension URI ('https://autoagentprotocol.org/extensions/a2a-automotive-retail/v1.0') and reflected in schema $id URLs; it is NOT repeated on the wire. Responses additionally carry a 'data' object and an optional 'message' note. Errors use the Error schema instead.
    """

    type: str = pydantic.Field()
    """
    AAP message type identifier. For skill calls: '<scope>.<thing>.request' or '<scope>.<thing>.response' (e.g. 'inventory.search.request', 'lead.appointment.response'). For envelopes: 'aap.event', 'aap.error'.
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Response payload (responses only). Requests carry their fields at the top level next to 'type'.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional contextual note from the dealer or LLM, intended for the buyer agent or end user. MAY be absent or empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
