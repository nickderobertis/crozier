

import typing

LaunchLayerControlPlaneProviderUpdate = typing.Dict[str, typing.Any]
"""
All LaunchLayer control-plane fields are fixed at creation: a request
carrying one is rejected with 400. A body echoed from GET must have
them stripped.
"""
