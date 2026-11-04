

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class TaxonomiesListResponseItemLinks(UniversalBaseModel):
    """
    URLs to alternative representations of the taxonomy entity.
    """

    parents: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of links to to this taxonomy's parents. This field is deprecated as of verson 2.4.
    """

    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="A link to the detail page for the taxonomy."),
    ] = None
    """
    A link to the detail page for the taxonomy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
