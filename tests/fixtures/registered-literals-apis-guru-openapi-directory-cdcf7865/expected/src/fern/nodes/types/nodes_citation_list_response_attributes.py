

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesCitationListResponseAttributes(UniversalBaseModel):
    """
    The properties of the citation entity.
    """

    author: typing.Optional[str] = pydantic.Field(default=None)
    """
    The list of bibliographic authors, represented as dictionaries of their given and family names, for the entitiy being cited.
    """

    doi: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DOI for the entity being cited, if one exists.
    """

    publisher: typing.Optional[str] = pydantic.Field(default=None)
    """
    The publisher of the entity being cited. For nodes and registrations, the publisher is the 'Open Science Framework'. For preprints, the publisher is the same as the preprint provider.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the entity being cited.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
