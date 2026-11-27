

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dna_annotation import DnaAnnotation


class DnaOligoHelm(UniversalBaseModel):
    helm: typing.Optional[str] = pydantic.Field(default=None)
    """
    Representation of the oligo in HELM syntax, including any chemical modifications
    """

    annotations: typing.Optional[typing.List[DnaAnnotation]] = pydantic.Field(default=None)
    """
    Annotations on the Oligo.
    """

    api_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiURL"),
        pydantic.Field(alias="apiURL", description="The canonical url of the Oligo in the API."),
    ] = None
    """
    The canonical url of the Oligo in the API.
    """

    bases: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base pairs of the Oligo.
    """

    custom_notation: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="customNotation"),
        pydantic.Field(
            alias="customNotation",
            description="Representation of the oligo in the custom notation specified in the request. Null if no notation was specified.",
        ),
    ] = None
    """
    Representation of the oligo in the custom notation specified in the request. Null if no notation was specified.
    """

    custom_notation_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="customNotationName"),
        pydantic.Field(
            alias="customNotationName",
            description="Name of the custom notation specified in the request. Null if no notation was specified.",
        ),
    ] = None
    """
    Name of the custom notation specified in the request. Null if no notation was specified.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
