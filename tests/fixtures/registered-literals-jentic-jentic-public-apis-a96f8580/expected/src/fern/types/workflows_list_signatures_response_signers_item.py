

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_list_signatures_response_signers_item_delegates_item import (
    WorkflowsListSignaturesResponseSignersItemDelegatesItem,
)


class WorkflowsListSignaturesResponseSignersItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    email: typing.Optional[str] = None
    role_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="roleName"), pydantic.Field(alias="roleName")
    ] = None
    signature_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signatureStatus"), pydantic.Field(alias="signatureStatus")
    ] = None
    delegates: typing.Optional[typing.List[WorkflowsListSignaturesResponseSignersItemDelegatesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
