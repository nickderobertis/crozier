

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mscid import Mscid
from .uri import Uri


class InvRelation(UniversalBaseModel):
    id: typing_extensions.Annotated[typing.Optional[Mscid], FieldMetadata(alias="@id"), pydantic.Field(alias="@id")] = (
        None
    )
    uri: typing.Optional[Uri] = None
    child_schemes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="child schemes"),
        pydantic.Field(
            alias="child schemes",
            description="Schemes that are profiles of the current scheme. In practice, this means either that the child scheme explicitly “borrows” elements from the current scheme, or that all instances of the child scheme would be valid instances of the current scheme.",
        ),
    ] = None
    """
    Schemes that are profiles of the current scheme. In practice, this means either that the child scheme explicitly “borrows” elements from the current scheme, or that all instances of the child scheme would be valid instances of the current scheme.
    """

    tools: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tools that either accept metadata conforming to the current scheme as input, or output such metadata.
    """

    input_to_mappings: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="input to mappings"),
        pydantic.Field(
            alias="input to mappings",
            description="Mappings that may be used to convert records conforming to the current scheme into records conforming to other schemes.",
        ),
    ] = None
    """
    Mappings that may be used to convert records conforming to the current scheme into records conforming to other schemes.
    """

    output_from_mappings: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="output from mappings"),
        pydantic.Field(
            alias="output from mappings",
            description="Mappings that can be used to convert records conforming to another scheme into records conforming to the current schemes.",
        ),
    ] = None
    """
    Mappings that can be used to convert records conforming to another scheme into records conforming to the current schemes.
    """

    endorsements: typing.Optional[typing.List[str]] = None
    maintained_resources: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="maintained resources"),
        pydantic.Field(
            alias="maintained resources",
            description="Schemes, tools and mappings maintained by the current organization.",
        ),
    ] = None
    """
    Schemes, tools and mappings maintained by the current organization.
    """

    funded_resources: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="funded resources"),
        pydantic.Field(
            alias="funded resources", description="Schemes, tools and mappings funded by the current organization."
        ),
    ] = None
    """
    Schemes, tools and mappings funded by the current organization.
    """

    used_schemes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="used schemes"),
        pydantic.Field(
            alias="used schemes", description="Schemes that are known to be used by the current organization."
        ),
    ] = None
    """
    Schemes that are known to be used by the current organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
