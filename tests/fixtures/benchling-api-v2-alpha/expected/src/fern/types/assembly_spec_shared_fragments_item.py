

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .assembly_fragment_shared import AssemblyFragmentShared


class AssemblySpecSharedFragmentsItem(AssemblyFragmentShared):
    bin_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="binId"), pydantic.Field(alias="binId", description="ID of the fragment's bin")
    ]
    """
    ID of the fragment's bin
    """

    preferred_primer3id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="preferredPrimer3Id"),
        pydantic.Field(
            alias="preferredPrimer3Id",
            description="API identifier of a Benchling oligo to be used as a primer at the 3' end of the fragment.",
        ),
    ] = None
    """
    API identifier of a Benchling oligo to be used as a primer at the 3' end of the fragment.
    """

    preferred_primer5id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="preferredPrimer5Id"),
        pydantic.Field(
            alias="preferredPrimer5Id",
            description="API identifier of a Benchling oligo to be used as a primer at the 5' end of the fragment.",
        ),
    ] = None
    """
    API identifier of a Benchling oligo to be used as a primer at the 5' end of the fragment.
    """

    restriction_enzyme3id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="restrictionEnzyme3Id"),
        pydantic.Field(alias="restrictionEnzyme3Id", description="ID of enzyme used to digest fragment at 3' end"),
    ] = None
    """
    ID of enzyme used to digest fragment at 3' end
    """

    restriction_enzyme5id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="restrictionEnzyme5Id"),
        pydantic.Field(alias="restrictionEnzyme5Id", description="ID of enzyme used to digest fragment at 5' end"),
    ] = None
    """
    ID of enzyme used to digest fragment at 5' end
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
