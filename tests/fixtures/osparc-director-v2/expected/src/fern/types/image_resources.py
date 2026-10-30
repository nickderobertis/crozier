

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .boot_mode import BootMode
from .resource_value import ResourceValue


class ImageResources(UniversalBaseModel):
    image: str = pydantic.Field()
    """
    Used by the frontend to provide a context for the users.Services with a docker-compose spec will have multiple entries.Using the `image:version` instead of the docker-compose spec is more helpful for the end user.
    """

    resources: typing.Dict[str, ResourceValue]
    boot_modes: typing.Optional[typing.List[BootMode]] = pydantic.Field(default=None)
    """
    describe how a service shall be booted, using CPU, MPI, openMP or GPU
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
