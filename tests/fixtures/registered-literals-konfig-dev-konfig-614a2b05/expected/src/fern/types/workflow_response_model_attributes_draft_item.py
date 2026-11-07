

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflow_response_model_attributes_draft_item_last_modified import (
    WorkflowResponseModelAttributesDraftItemLastModified,
)


class WorkflowResponseModelAttributesDraftItem(UniversalBaseModel):
    version: typing.Optional[str] = None
    version_number: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="versionNumber"), pydantic.Field(alias="versionNumber")
    ] = None
    filename: typing.Optional[str] = None
    download: typing.Optional[str] = None
    last_modified: typing_extensions.Annotated[
        typing.Optional[WorkflowResponseModelAttributesDraftItemLastModified],
        FieldMetadata(alias="lastModified"),
        pydantic.Field(alias="lastModified"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
