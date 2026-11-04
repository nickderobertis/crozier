

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .registrations_citations_list_response_item_attributes import RegistrationsCitationsListResponseItemAttributes


class RegistrationsCitationsListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[RegistrationsCitationsListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the citation style entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the citation style, e.g. APA.
    """

    links: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the citation style entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the citation style entity (`citation-styles`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
