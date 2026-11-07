

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .preprints_bibliographic_contributors_list_response_item_attributes_permission import (
    PreprintsBibliographicContributorsListResponseItemAttributesPermission,
)


class PreprintsBibliographicContributorsListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the contributor entity.
    """

    bibliographic: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the contributor will be included in citations for the Preprint. The default value is true.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The position of this contributor in the list of Preprint's contributors and in a Preprint's citations.
    """

    permission: typing.Optional[PreprintsBibliographicContributorsListResponseItemAttributesPermission] = (
        pydantic.Field(default=None)
    )
    """
    The permission level of the contributor. The default value is 'write'.
    """

    unregistered_contributor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The assigned name of the contributor if the contributor has not yet claimed their account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
