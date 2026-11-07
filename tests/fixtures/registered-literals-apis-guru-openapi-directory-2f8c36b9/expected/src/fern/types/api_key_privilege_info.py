

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiKeyPrivilegeInfo(UniversalBaseModel):
    allows_billable_operations: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowsBillableOperations"),
        pydantic.Field(alias="allowsBillableOperations"),
    ] = None
    help_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="helpText"), pydantic.Field(alias="helpText")
    ] = None
    id4n_associated: typing_extensions.Annotated[
        bool, FieldMetadata(alias="id4nAssociated"), pydantic.Field(alias="id4nAssociated")
    ]
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
