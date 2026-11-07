

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_preprints_list_response_item_attributes import UsersPreprintsListResponseItemAttributes
from .users_preprints_list_response_item_links import UsersPreprintsListResponseItemLinks
from .users_preprints_list_response_item_relationships import UsersPreprintsListResponseItemRelationships


class UsersPreprintsListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[UsersPreprintsListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the preprint entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the preprint entity.
    """

    links: typing.Optional[UsersPreprintsListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the preprint entity.
    """

    relationships: UsersPreprintsListResponseItemRelationships = pydantic.Field()
    """
    URLs to other entities or entity collections that have a relationship to the preprint entity.
    """

    type: str = pydantic.Field()
    """
    The type identifier of the preprint entity (`preprints`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
