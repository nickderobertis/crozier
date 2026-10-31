

import typing

LaunchLayerNodePoolProviderUpdate = typing.Dict[str, typing.Any]
"""
All LaunchLayer node-pool fields (instanceType, hostOSProfile, vmProfile,
fulfillmentStrategy, securityGroupRefs, securityGroups) are fixed at creation: a request
carrying one is rejected with 400. A body echoed from GET must have them
stripped.
"""
