

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .parameter import Parameter
from .user_defined_additional_node_fields import UserDefinedAdditionalNodeFields


class NodeDataSplit(UniversalBaseModel):
    id: str
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    branch_parameters_template: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]],
        FieldMetadata(alias="branchParametersTemplate"),
        pydantic.Field(alias="branchParametersTemplate"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
