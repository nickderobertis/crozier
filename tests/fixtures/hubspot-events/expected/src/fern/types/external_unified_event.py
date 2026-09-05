

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExternalUnifiedEvent(UniversalBaseModel):
    """
    Used to represent any event. With this format, the `objectType` and `eventType` values are stringified CRM types. Example object:
    <br/>
    ```
     {
          "objectType": "CONTACT",
          "objectId": 208451632,
          "eventType": "e_visited_page",
          "occurredAt": 1567377501421,
          "id": "leviathan-be3335d3-46f1-3985-988e-ff38e6e7b9d8",
          "properties": {
              "hs_url": "https://some-website.com/",
              "hs_title": "Home",
              "hs_referrer": "https://some-other-website.com/blog/why-we-love-big-data-and-you-should-too",
              "hs_userAgent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
              "hs_city": "lund",
              "hs_region": "m",
              "hs_country": "se",
              "hs_session_id" : "leviathan-be3335d3-46f1-3985-988e-ff38e6e7b9d8",
              "hs_session_source" : "DIRECT"
          }
      }
    ```
    """

    event_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="eventType"),
        pydantic.Field(
            alias="eventType",
            description="The format of the `eventType` string is `ae{appId}_{eventTypeLabel}`, `pe{portalId}_{eventTypeLabel}`, or just `e_{eventTypeLabel}` for HubSpot events.",
        ),
    ]
    """
    The format of the `eventType` string is `ae{appId}_{eventTypeLabel}`, `pe{portalId}_{eventTypeLabel}`, or just `e_{eventTypeLabel}` for HubSpot events.
    """

    id: str = pydantic.Field()
    """
    A unique identifier for the event.
    """

    object_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="objectId"),
        pydantic.Field(alias="objectId", description="The objectId of the object which did the event."),
    ]
    """
    The objectId of the object which did the event.
    """

    object_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="objectType"),
        pydantic.Field(alias="objectType", description="The objectType for the object which did the event."),
    ]
    """
    The objectType for the object which did the event.
    """

    occurred_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="occurredAt"),
        pydantic.Field(alias="occurredAt", description="An ISO 8601 timestamp when the event occurred."),
    ]
    """
    An ISO 8601 timestamp when the event occurred.
    """

    properties: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
