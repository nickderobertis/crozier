

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_definition_mutation_graph_ql_type_input_webhook_headers_item import (
    ActionDefinitionMutationGraphQlTypeInputWebhookHeadersItem,
)
from .action_definition_mutation_graph_ql_type_input_webhook_kind import (
    ActionDefinitionMutationGraphQlTypeInputWebhookKind,
)
from .action_definition_mutation_graph_ql_type_input_webhook_request_transform import (
    ActionDefinitionMutationGraphQlTypeInputWebhookRequestTransform,
)
from .action_definition_mutation_graph_ql_type_input_webhook_response_transform import (
    ActionDefinitionMutationGraphQlTypeInputWebhookResponseTransform,
)
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


class ActionMetadataDefinition_Query(UniversalBaseModel):
    type: typing.Literal["query"] = "query"
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


class ActionMetadataDefinition_Mutation(UniversalBaseModel):
    type: typing.Literal["mutation"] = "mutation"
    arguments: typing.Optional[typing.List[ArgumentDefinitionGraphQlType]] = None
    forward_client_headers: typing.Optional[bool] = None
    handler: str
    headers: typing.Optional[typing.List[ActionDefinitionMutationGraphQlTypeInputWebhookHeadersItem]] = None
    ignored_client_headers: typing.Optional[typing.List[str]] = None
    kind: typing.Optional[ActionDefinitionMutationGraphQlTypeInputWebhookKind] = None
    output_type: str
    request_transform: typing.Optional[ActionDefinitionMutationGraphQlTypeInputWebhookRequestTransform] = None
    response_transform: typing.Optional[ActionDefinitionMutationGraphQlTypeInputWebhookResponseTransform] = None
    timeout: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ActionMetadataDefinition = typing_extensions.Annotated[
    typing.Union[ActionMetadataDefinition_Query, ActionMetadataDefinition_Mutation],
    pydantic.Field(discriminator="type"),
]
