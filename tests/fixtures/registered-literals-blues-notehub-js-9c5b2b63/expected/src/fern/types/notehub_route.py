

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .aws_route import AwsRoute
from .azure_route import AzureRoute
from .blynk_route import BlynkRoute
from .datacake_route import DatacakeRoute
from .google_route import GoogleRoute
from .http_route import HttpRoute
from .mqtt_route import MqttRoute
from .proxy_route import ProxyRoute
from .qubitro_route import QubitroRoute
from .rad_route import RadRoute
from .s3archive_route import S3ArchiveRoute
from .slack_route import SlackRoute
from .snowflake_route import SnowflakeRoute
from .snowpipe_streaming_route import SnowpipeStreamingRoute
from .thingworx_route import ThingworxRoute
from .twilio_route import TwilioRoute


class NotehubRoute(UniversalBaseModel):
    """
    Route resource as stored/returned by the server.
    """

    aws: typing.Optional[AwsRoute] = None
    azure: typing.Optional[AzureRoute] = None
    blynk: typing.Optional[BlynkRoute] = None
    datacake: typing.Optional[DatacakeRoute] = None
    disabled: typing.Optional[bool] = None
    google: typing.Optional[GoogleRoute] = None
    http: typing.Optional[HttpRoute] = None
    label: typing.Optional[str] = None
    modified: typing.Optional[dt.datetime] = None
    mqtt: typing.Optional[MqttRoute] = None
    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional free-form text for annotating the route.
    """

    proxy: typing.Optional[ProxyRoute] = None
    qubitro: typing.Optional[QubitroRoute] = None
    radnote: typing.Optional[RadRoute] = None
    s3archive: typing.Optional[S3ArchiveRoute] = None
    slack: typing.Optional[SlackRoute] = None
    snowflake: typing.Optional[SnowflakeRoute] = None
    snowpipe_streaming: typing.Optional[SnowpipeStreamingRoute] = None
    thingworx: typing.Optional[ThingworxRoute] = None
    twilio: typing.Optional[TwilioRoute] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Mirrors hublib.RouteType.
    """

    uid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
