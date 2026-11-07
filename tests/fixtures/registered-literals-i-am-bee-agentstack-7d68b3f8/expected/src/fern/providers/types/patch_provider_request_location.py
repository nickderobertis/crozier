

import typing

from ...types.docker_image_provider_location import DockerImageProviderLocation
from ...types.network_provider_location import NetworkProviderLocation

PatchProviderRequestLocation = typing.Union[DockerImageProviderLocation, NetworkProviderLocation]
