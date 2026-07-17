

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DetectStackResourceDriftOutputStackResourceDriftModuleInfo(UniversalBaseModel):
    """
    Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.
    """

    type_hierarchy: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeHierarchy"),
        pydantic.Field(
            alias="TypeHierarchy",
            description="<p>A concatenated list of the module type or types containing the resource. Module types are listed starting with the inner-most nested module, and separated by <code>/</code>.</p> <p>In the following example, the resource was created from a module of type <code>AWS::First::Example::MODULE</code>, that's nested inside a parent module of type <code>AWS::Second::Example::MODULE</code>.</p> <p> <code>AWS::First::Example::MODULE/AWS::Second::Example::MODULE</code> </p>",
        ),
    ] = None
    """
    <p>A concatenated list of the module type or types containing the resource. Module types are listed starting with the inner-most nested module, and separated by <code>/</code>.</p> <p>In the following example, the resource was created from a module of type <code>AWS::First::Example::MODULE</code>, that's nested inside a parent module of type <code>AWS::Second::Example::MODULE</code>.</p> <p> <code>AWS::First::Example::MODULE/AWS::Second::Example::MODULE</code> </p>
    """

    logical_id_hierarchy: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LogicalIdHierarchy"),
        pydantic.Field(
            alias="LogicalIdHierarchy",
            description='<p>A concatenated list of the logical IDs of the module or modules containing the resource. Modules are listed starting with the inner-most nested module, and separated by <code>/</code>.</p> <p>In the following example, the resource was created from a module, <code>moduleA</code>, that\'s nested inside a parent module, <code>moduleB</code>.</p> <p> <code>moduleA/moduleB</code> </p> <p>For more information, see <a href="AWSCloudFormation/latest/UserGuide/modules.html#module-ref-resources">Referencing resources in a module</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>A concatenated list of the logical IDs of the module or modules containing the resource. Modules are listed starting with the inner-most nested module, and separated by <code>/</code>.</p> <p>In the following example, the resource was created from a module, <code>moduleA</code>, that's nested inside a parent module, <code>moduleB</code>.</p> <p> <code>moduleA/moduleB</code> </p> <p>For more information, see <a href="AWSCloudFormation/latest/UserGuide/modules.html#module-ref-resources">Referencing resources in a module</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
