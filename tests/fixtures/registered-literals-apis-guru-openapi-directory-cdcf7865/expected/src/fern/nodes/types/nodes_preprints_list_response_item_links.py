

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class NodesPreprintsListResponseItemLinks(UniversalBaseModel):
    """
    URLs to alternative representations of the preprint entity.
    """

    doi: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL representation of the DOI entered by the user for the preprint manuscript.
    """

    html: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the project on the OSF that was created for the preprint, or from which the preprint was created.
    """

    preprint_doi: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL representation of the OSF assigned DOI for the preprint.
    """

    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="A link to the detail page for the preprint."),
    ] = None
    """
    A link to the detail page for the preprint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
