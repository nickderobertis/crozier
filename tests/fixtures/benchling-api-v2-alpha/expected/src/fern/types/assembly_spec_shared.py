

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assembly_spec_shared_assembly_parameters import AssemblySpecSharedAssemblyParameters
from .assembly_spec_shared_bins_item import AssemblySpecSharedBinsItem
from .assembly_spec_shared_constructs_item import AssemblySpecSharedConstructsItem
from .assembly_spec_shared_fragments_item import AssemblySpecSharedFragmentsItem
from .assembly_spec_shared_topology import AssemblySpecSharedTopology


class AssemblySpecShared(UniversalBaseModel):
    """
    Information required when validating or finalizing a bulk assembly.
    """

    assembly_parameters: typing_extensions.Annotated[
        AssemblySpecSharedAssemblyParameters,
        FieldMetadata(alias="assemblyParameters"),
        pydantic.Field(
            alias="assemblyParameters",
            description="Assembly-wide parameters to describe requirements and procedures for the assembly.",
        ),
    ]
    """
    Assembly-wide parameters to describe requirements and procedures for the assembly.
    """

    bins: typing.List[AssemblySpecSharedBinsItem] = pydantic.Field()
    """
    Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.
    """

    constructs: typing.List[AssemblySpecSharedConstructsItem] = pydantic.Field()
    """
    Output constructs that should be created.
    """

    fragments: typing.List[AssemblySpecSharedFragmentsItem] = pydantic.Field()
    """
    Fragments to be used in the assembly.
    """

    topology: AssemblySpecSharedTopology = pydantic.Field()
    """
    Whether the created constructs should be circular or linear.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
