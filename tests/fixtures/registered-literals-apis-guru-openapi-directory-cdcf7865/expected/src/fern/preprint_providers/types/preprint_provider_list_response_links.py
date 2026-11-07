

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PreprintProviderListResponseLinks(UniversalBaseModel):
    """
    Links to alternative representations of the preprint entity.
    """

    external_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the external website for the preprint provider.
    """

    preprints: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the preprint list page for the preprint provider.
    """

    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="A link to the detail page for the preprint provider."),
    ] = None
    """
    A link to the detail page for the preprint provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
