

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .branch_parameters import BranchParameters
from .parameter import Parameter
from .user_defined_additional_node_fields import UserDefinedAdditionalNodeFields


class NodeDataJoin(UniversalBaseModel):
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    branch_parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[BranchParameters]],
        FieldMetadata(alias="branchParameters"),
        pydantic.Field(alias="branchParameters"),
    ] = None
    branch_parameters_template: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]],
        FieldMetadata(alias="branchParametersTemplate"),
        pydantic.Field(alias="branchParametersTemplate"),
    ] = None
    id: str
    node_type: typing_extensions.Annotated[str, FieldMetadata(alias="nodeType"), pydantic.Field(alias="nodeType")]
    output_var: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="outputVar"), pydantic.Field(alias="outputVar")
    ] = None
    parameters: typing.Optional[typing.List[Parameter]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
