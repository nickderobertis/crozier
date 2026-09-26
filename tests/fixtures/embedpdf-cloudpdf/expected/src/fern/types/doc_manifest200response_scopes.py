

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_manifest200response_scopes_actions import DocManifest200ResponseScopesActions
from .doc_manifest200response_scopes_annotations import DocManifest200ResponseScopesAnnotations
from .doc_manifest200response_scopes_attachments import DocManifest200ResponseScopesAttachments
from .doc_manifest200response_scopes_content import DocManifest200ResponseScopesContent
from .doc_manifest200response_scopes_layout import DocManifest200ResponseScopesLayout
from .doc_manifest200response_scopes_metadata import DocManifest200ResponseScopesMetadata


class DocManifest200ResponseScopes(UniversalBaseModel):
    content: DocManifest200ResponseScopesContent
    annotations: DocManifest200ResponseScopesAnnotations
    layout: DocManifest200ResponseScopesLayout
    attachments: DocManifest200ResponseScopesAttachments
    metadata: DocManifest200ResponseScopesMetadata
    actions: DocManifest200ResponseScopesActions

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
