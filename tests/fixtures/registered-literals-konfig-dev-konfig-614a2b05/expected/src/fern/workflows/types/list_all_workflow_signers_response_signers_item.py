

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_workflow_signers_response_signers_item_delegates_item import (
    ListAllWorkflowSignersResponseSignersItemDelegatesItem,
)


class ListAllWorkflowSignersResponseSignersItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    email: typing.Optional[str] = None
    role_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="roleName"), pydantic.Field(alias="roleName")
    ] = None
    signature_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signatureStatus"), pydantic.Field(alias="signatureStatus")
    ] = None
    delegates: typing.Optional[typing.List[ListAllWorkflowSignersResponseSignersItemDelegatesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
