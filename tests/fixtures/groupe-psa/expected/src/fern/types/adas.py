

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .adas_artiv import AdasArtiv
from .adas_bsm import AdasBsm
from .adas_llka import AdasLlka
from .adas_park_assist import AdasParkAssist
from .adas_rgi import AdasRgi
from .adas_rlka import AdasRlka


class Adas(UniversalBaseModel):
    park_assist: typing_extensions.Annotated[
        typing.Optional[AdasParkAssist], FieldMetadata(alias="parkAssist"), pydantic.Field(alias="parkAssist")
    ] = None
    accr: typing.Optional[str] = pydantic.Field(default=None)
    """
    Adaptive Cruise Control Regulation
    """

    lvv: typing.Optional[bool] = None
    rvv: typing.Optional[str] = pydantic.Field(default=None)
    """
    Advanced Speed Regulator
    """

    aebs: typing.Optional[str] = pydantic.Field(default=None)
    """
    Advanced Emergency Braking System
    """

    afil: typing.Optional[str] = pydantic.Field(default=None)
    """
    Lane Departure Warning System
    """

    artiv: typing.Optional[AdasArtiv] = pydantic.Field(default=None)
    """
    Respect of inter vehicle time assist (ARTIV)
    """

    bsm: typing.Optional[AdasBsm] = pydantic.Field(default=None)
    """
    Blind Spot Monitoring
    """

    esp: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Electronic Stability Program
    """

    abs: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Anti-lock braking system
    """

    fse: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Electric brake service
    """

    sli: typing.Optional[int] = pydantic.Field(default=None)
    """
    Speed Limit Information (expressed in km/h)
    """

    rlka: typing.Optional[AdasRlka] = pydantic.Field(default=None)
    """
    Right Lane Keeping Assist
    """

    llka: typing.Optional[AdasLlka] = pydantic.Field(default=None)
    """
    Left Lane Keeping Assist
    """

    rgi: typing.Optional[AdasRgi] = pydantic.Field(default=None)
    """
    Recommended gear indicator
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
