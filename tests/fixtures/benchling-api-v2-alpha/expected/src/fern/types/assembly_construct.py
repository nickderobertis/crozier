

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assembly_construct_construct_primers_item import AssemblyConstructConstructPrimersItem
from .assembly_polymer_reference import AssemblyPolymerReference


class AssemblyConstruct(UniversalBaseModel):
    construct_fragment_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="constructFragmentIds"),
        pydantic.Field(alias="constructFragmentIds"),
    ] = None
    construct_primers: typing_extensions.Annotated[
        typing.Optional[typing.List[AssemblyConstructConstructPrimersItem]],
        FieldMetadata(alias="constructPrimers"),
        pydantic.Field(alias="constructPrimers"),
    ] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the construct.
    """

    output_polymer: typing_extensions.Annotated[
        typing.Optional[AssemblyPolymerReference],
        FieldMetadata(alias="outputPolymer"),
        pydantic.Field(alias="outputPolymer"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
