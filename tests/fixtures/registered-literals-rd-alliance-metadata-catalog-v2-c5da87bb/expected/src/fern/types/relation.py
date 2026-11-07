

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mscid import Mscid


class Relation(UniversalBaseModel):
    id: typing_extensions.Annotated[typing.Optional[Mscid], FieldMetadata(alias="@id"), pydantic.Field(alias="@id")] = (
        None
    )
    parent_schemes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="parent schemes"),
        pydantic.Field(
            alias="parent schemes",
            description="Schemes of which the current scheme is a profile. In practice, this means either that the current scheme explicitly “borrows” elements from the parent scheme, or that all instances of the current scheme would be valid instances of the parent scheme.",
        ),
    ] = None
    """
    Schemes of which the current scheme is a profile. In practice, this means either that the current scheme explicitly “borrows” elements from the parent scheme, or that all instances of the current scheme would be valid instances of the parent scheme.
    """

    supported_schemes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="supported schemes"),
        pydantic.Field(
            alias="supported schemes",
            description="Schemes to which the tool’s input metadata should conform, or output metadata does conform.",
        ),
    ] = None
    """
    Schemes to which the tool’s input metadata should conform, or output metadata does conform.
    """

    input_schemes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="input schemes"),
        pydantic.Field(
            alias="input schemes",
            description="Schemes to which a metadata record input to the current mapping must conform.",
        ),
    ] = None
    """
    Schemes to which a metadata record input to the current mapping must conform.
    """

    output_schemes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="output schemes"),
        pydantic.Field(
            alias="output schemes",
            description="Schemes to which metadata records output from the current mapping conform.",
        ),
    ] = None
    """
    Schemes to which metadata records output from the current mapping conform.
    """

    endorsed_schemes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="endorsed schemes"),
        pydantic.Field(alias="endorsed schemes", description="Schemes endorsed by the current endorsement."),
    ] = None
    """
    Schemes endorsed by the current endorsement.
    """

    maintainers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Organizations that maintain the current scheme, tool or mapping.
    """

    funders: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Organizations that fund the current scheme, tool or mapping.
    """

    users: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Organizations that are known to use the current scheme.
    """

    originators: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Organizations that have made the current endorsement.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
