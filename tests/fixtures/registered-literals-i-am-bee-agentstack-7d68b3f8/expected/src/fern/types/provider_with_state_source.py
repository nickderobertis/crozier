

import typing

from .docker_image_provider_location import DockerImageProviderLocation
from .network_provider_location import NetworkProviderLocation

ProviderWithStateSource = typing.Union[DockerImageProviderLocation, NetworkProviderLocation]
