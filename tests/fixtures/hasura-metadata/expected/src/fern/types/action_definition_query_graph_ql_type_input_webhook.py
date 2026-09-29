

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_definition_query_graph_ql_type_input_webhook_headers_item import (
    ActionDefinitionQueryGraphQlTypeInputWebhookHeadersItem,
)
from .action_definition_query_graph_ql_type_input_webhook_request_transform import (
    ActionDefinitionQueryGraphQlTypeInputWebhookRequestTransform,
)
from .action_definition_query_graph_ql_type_input_webhook_response_transform import (
    ActionDefinitionQueryGraphQlTypeInputWebhookResponseTransform,
)
from .argument_definition_graph_ql_type import ArgumentDefinitionGraphQlType


class ActionDefinitionQueryGraphQlTypeInputWebhook(UniversalBaseModel):
    arguments: typing.Optional[typing.List[ArgumentDefinitionGraphQlType]] = None
    forward_client_headers: typing.Optional[bool] = None
    handler: str
    headers: typing.Optional[typing.List[ActionDefinitionQueryGraphQlTypeInputWebhookHeadersItem]] = None
    ignored_client_headers: typing.Optional[typing.List[str]] = None
    output_type: str
    request_transform: typing.Optional[ActionDefinitionQueryGraphQlTypeInputWebhookRequestTransform] = None
    response_transform: typing.Optional[ActionDefinitionQueryGraphQlTypeInputWebhookResponseTransform] = None
    timeout: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
