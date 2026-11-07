

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .registrations_logs_list_response_item_attributes import RegistrationsLogsListResponseItemAttributes
from .registrations_logs_list_response_item_links import RegistrationsLogsListResponseItemLinks
from .registrations_logs_list_response_item_relationships import RegistrationsLogsListResponseItemRelationships


class RegistrationsLogsListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[RegistrationsLogsListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the log.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the log.
    """

    links: typing.Optional[RegistrationsLogsListResponseItemLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the log entity.
    """

    relationships: typing.Optional[RegistrationsLogsListResponseItemRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the log.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the log (`logs`)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
