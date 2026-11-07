

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PreprintProviderListResponseRelationships(UniversalBaseModel):
    """
    Links to other entities or entity collections that have a relationship to the preprint provider.
    """

    licenses_acceptable: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to licenses the preprint provider allows.
    """

    preprints: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the preprint list page for the preprint provider.
    """

    taxonomies: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the taxonomies the preprint provider allows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
