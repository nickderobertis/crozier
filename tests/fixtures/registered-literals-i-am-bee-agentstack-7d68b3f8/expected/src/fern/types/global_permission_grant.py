

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .global_permission_grant_a2a_proxy import GlobalPermissionGrantA2AProxy
from .global_permission_grant_connectors_item import GlobalPermissionGrantConnectorsItem
from .global_permission_grant_context_data_item import GlobalPermissionGrantContextDataItem
from .global_permission_grant_contexts_item import GlobalPermissionGrantContextsItem
from .global_permission_grant_embeddings_item import GlobalPermissionGrantEmbeddingsItem
from .global_permission_grant_feedback_item import GlobalPermissionGrantFeedbackItem
from .global_permission_grant_files_item import GlobalPermissionGrantFilesItem
from .global_permission_grant_llm_item import GlobalPermissionGrantLlmItem
from .global_permission_grant_model_providers_item import GlobalPermissionGrantModelProvidersItem
from .global_permission_grant_provider_variables_item import GlobalPermissionGrantProviderVariablesItem
from .global_permission_grant_providers_item import GlobalPermissionGrantProvidersItem
from .global_permission_grant_vector_stores_item import GlobalPermissionGrantVectorStoresItem


class GlobalPermissionGrant(UniversalBaseModel):
    files: typing.Optional[typing.List[GlobalPermissionGrantFilesItem]] = None
    feedback: typing.Optional[typing.List[GlobalPermissionGrantFeedbackItem]] = None
    vector_stores: typing.Optional[typing.List[GlobalPermissionGrantVectorStoresItem]] = None
    llm: typing.Optional[typing.List[GlobalPermissionGrantLlmItem]] = None
    embeddings: typing.Optional[typing.List[GlobalPermissionGrantEmbeddingsItem]] = None
    model_providers: typing.Optional[typing.List[GlobalPermissionGrantModelProvidersItem]] = None
    a2a_proxy: typing.Optional[GlobalPermissionGrantA2AProxy] = None
    providers: typing.Optional[typing.List[GlobalPermissionGrantProvidersItem]] = None
    provider_variables: typing.Optional[typing.List[GlobalPermissionGrantProviderVariablesItem]] = None
    contexts: typing.Optional[typing.List[GlobalPermissionGrantContextsItem]] = None
    context_data: typing.Optional[typing.List[GlobalPermissionGrantContextDataItem]] = None
    connectors: typing.Optional[typing.List[GlobalPermissionGrantConnectorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
