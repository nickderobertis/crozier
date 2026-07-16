

import typing

from .api import Api

ApIs = typing.Dict[str, Api]
"""
List of API details.
It is a JSON object with API IDs(`<provider>[:<service>]`) as keys.
"""
