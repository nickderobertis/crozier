

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1CompanyTic(UniversalBaseModel):
    """
    Integration metadata (internal only). Present for synced clients.
    """

    uri: str = pydantic.Field()
    """
    Canonical TIC identifier (e.g., tic://jira/workspace-id/clients/abc123). Immutable once set.
    """

    tool_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Original external tool identifier (e.g., jira, trello, asana).
    """

    external_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Direct link to the client in the external tool.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
