

import typing

from .bot_services_item_base_url import BotServicesItemBaseUrl
from .bot_services_item_config_data import BotServicesItemConfigData

BotServicesItem = typing.Union[BotServicesItemBaseUrl, BotServicesItemConfigData]
