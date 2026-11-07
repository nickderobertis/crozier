

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .branch_end_definition import BranchEndDefinition
from .branch_parameters import BranchParameters
from .expression import Expression
from .field import Field
from .fragment_parameter import FragmentParameter
from .fragment_ref import FragmentRef
from .list_field import ListField
from .list_fragment_parameter import ListFragmentParameter
from .parameter import Parameter
from .service_ref import ServiceRef
from .sink_ref import SinkRef
from .source_ref import SourceRef
from .user_defined_additional_node_fields import UserDefinedAdditionalNodeFields
from .variable_operation_schema_type import VariableOperationSchemaType


class NodeData_Variable(UniversalBaseModel):
    type: typing.Literal["Variable"] = "Variable"
    id: str
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    operation: VariableOperationSchemaType
    variables_to_unset: typing_extensions.Annotated[
        typing.Optional[typing.List[Field]],
        FieldMetadata(alias="variablesToUnset"),
        pydantic.Field(alias="variablesToUnset"),
    ] = None
    var_name: typing_extensions.Annotated[str, FieldMetadata(alias="varName"), pydantic.Field(alias="varName")]
    value: Expression

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_VariableBuilder(UniversalBaseModel):
    type: typing.Literal["VariableBuilder"] = "VariableBuilder"
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
    id: str
    fields: typing.Optional[typing.List[Field]] = None
    var_name: typing_extensions.Annotated[str, FieldMetadata(alias="varName"), pydantic.Field(alias="varName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_BranchEndData(UniversalBaseModel):
    type: typing.Literal["BranchEndData"] = "BranchEndData"
    definition: BranchEndDefinition

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_CustomNode(UniversalBaseModel):
    type: typing.Literal["CustomNode"] = "CustomNode"
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


class NodeData_Enricher(UniversalBaseModel):
    type: typing.Literal["Enricher"] = "Enricher"
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
    id: str
    output: str
    service: ServiceRef

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_Filter(UniversalBaseModel):
    type: typing.Literal["Filter"] = "Filter"
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
    expression: Expression
    id: str
    is_disabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDisabled"), pydantic.Field(alias="isDisabled")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_FragmentInput(UniversalBaseModel):
    type: typing.Literal["FragmentInput"] = "FragmentInput"
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    id: str
    is_disabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDisabled"), pydantic.Field(alias="isDisabled")
    ] = None
    fragment_params: typing_extensions.Annotated[
        typing.Optional[typing.List[FragmentParameter]],
        FieldMetadata(alias="fragmentParams"),
        pydantic.Field(alias="fragmentParams"),
    ] = None
    ref: FragmentRef

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_FragmentInputDefinition(UniversalBaseModel):
    type: typing.Literal["FragmentInputDefinition"] = "FragmentInputDefinition"
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    id: str
    parameters: ListFragmentParameter

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_FragmentOutputDefinition(UniversalBaseModel):
    type: typing.Literal["FragmentOutputDefinition"] = "FragmentOutputDefinition"
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    id: str
    fields: ListField
    output_name: typing_extensions.Annotated[str, FieldMetadata(alias="outputName"), pydantic.Field(alias="outputName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_Join(UniversalBaseModel):
    type: typing.Literal["Join"] = "Join"
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


class NodeData_Processor(UniversalBaseModel):
    type: typing.Literal["Processor"] = "Processor"
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
    id: str
    is_disabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDisabled"), pydantic.Field(alias="isDisabled")
    ] = None
    service: ServiceRef

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_Sink(UniversalBaseModel):
    type: typing.Literal["Sink"] = "Sink"
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
    id: str
    is_disabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDisabled"), pydantic.Field(alias="isDisabled")
    ] = None
    ref: SinkRef

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_Source(UniversalBaseModel):
    type: typing.Literal["Source"] = "Source"
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
    ref: SourceRef

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NodeData_Split(UniversalBaseModel):
    type: typing.Literal["Split"] = "Split"
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


class NodeData_Switch(UniversalBaseModel):
    type: typing.Literal["Switch"] = "Switch"
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
    expression: typing.Optional[Expression] = None
    expr_val: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="exprVal"), pydantic.Field(alias="exprVal")
    ] = None
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


NodeData = typing_extensions.Annotated[
    typing.Union[
        NodeData_Variable,
        NodeData_VariableBuilder,
        NodeData_BranchEndData,
        NodeData_CustomNode,
        NodeData_Enricher,
        NodeData_Filter,
        NodeData_FragmentInput,
        NodeData_FragmentInputDefinition,
        NodeData_FragmentOutputDefinition,
        NodeData_Join,
        NodeData_Processor,
        NodeData_Sink,
        NodeData_Source,
        NodeData_Split,
        NodeData_Switch,
    ],
    pydantic.Field(discriminator="type"),
]
