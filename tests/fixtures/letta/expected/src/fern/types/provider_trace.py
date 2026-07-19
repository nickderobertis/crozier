

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProviderTrace(UniversalBaseModel):
    """
    Letta's internal representation of a provider trace.

    Attributes:
        id (str): The unique identifier of the provider trace.
        request_json (Dict[str, Any]): JSON content of the provider request.
        response_json (Dict[str, Any]): JSON content of the provider response.
        step_id (str): ID of the step that this trace is associated with.
        agent_id (str): ID of the agent that generated this trace.
        agent_tags (list[str]): Tags associated with the agent for filtering.
        call_type (str): Type of call (agent_step, summarization, etc.).
        run_id (str): ID of the run this trace is associated with.
        source (str): Source service that generated this trace (memgpt-server, lettuce-py).
        organization_id (str): The unique identifier of the organization.
        user_id (str): The unique identifier of the user who initiated the request.
        compaction_settings (Dict[str, Any]): Compaction/summarization settings (only for summarization calls).
        llm_config (Dict[str, Any]): LLM configuration used for this call (only for non-summarization calls).
        created_at (datetime): The timestamp when the object was created.
    """

    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was last updated.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Provider_trace
    """

    request_json: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    JSON content of the provider request
    """

    response_json: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    JSON content of the provider response
    """

    step_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the step that this trace is associated with
    """

    agent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the agent that generated this trace
    """

    agent_tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags associated with the agent for filtering
    """

    call_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of call (agent_step, summarization, etc.)
    """

    run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the run this trace is associated with
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source service that generated this trace (memgpt-server, lettuce-py)
    """

    org_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the organization
    """

    compaction_settings: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Compaction/summarization settings (summarization calls only)
    """

    llm_config: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    LLM configuration used for this call (non-summarization calls only)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
