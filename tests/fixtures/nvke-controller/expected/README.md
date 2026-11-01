# Fern Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Fern%2FPython)
[![pypi](https://img.shields.io/pypi/v/fern)](https://pypi.python.org/pypi/fern)

The Fern Python library provides convenient access to the Fern APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install fern
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from fern import FernApi, ClusterNetworkCreateConfig, NodePoolCreateConfig, NodeTaint, NodeTaintEffect, NicoNodePoolProvider, CreateClusterControlPlaneConfig, NicoControlPlaneProviderCreate, NicoClusterProvider

client = FernApi(
    token="<token>",
)

client.clusters.create_cluster(
    name="tenant-a-prod",
    control_plane_kubernetes_version="1.33.4",
    etcd_encrypted=True,
    network=ClusterNetworkCreateConfig(
        pod_cidr="192.168.0.0/16",
        service_cidr="10.96.0.0/12",
    ),
    node_pools=[
        NodePoolCreateConfig(
            name="gpu-workers",
            node_name_prefix="w",
            system_reserved_memory="16Gi",
            node_labels={
                "nvidia.com/gpu.present": "true"
            },
            node_taints=[
                NodeTaint(
                    key="nvidia.com/dedicated",
                    value="gpu",
                    effect=NodeTaintEffect.NO_SCHEDULE,
                )
            ],
            desired_node_count=2,
            recycle_budget=1,
            nico=NicoNodePoolProvider(
                vpc_prefix_i_ds=[
                    "2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"
                ],
                instance_type_id="0d2f4a6c-8e0b-4d2f-9a4c-6e8b0d2f4a6c",
                ssh_key_group_i_ds=[
                    "3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"
                ],
                release="example-ubuntu-24.04-amd64",
            ),
        )
    ],
    control_plane_config=CreateClusterControlPlaneConfig(
        desired_count=3,
        max_surge=1,
        system_reserved_memory="16Gi",
        nico=NicoControlPlaneProviderCreate(
            instance_type_preference=[
                "1c3e5a7f-9b1d-4f3e-a5c7-e9b1d3f5a7c9"
            ],
            vpc_prefix_i_ds=[
                "2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"
            ],
            release="example-ubuntu-24.04-amd64",
            ssh_key_group_i_ds=[
                "3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"
            ],
        ),
    ),
    nico=NicoClusterProvider(
        org_id="dipfedrcvjiw",
        site_id="4f6a8c2e-1b3d-4e5f-a7b9-c1d3e5f7a9b1",
        vpc_id="6a8c0e4f-3d5b-4f7a-b9c1-e3f5a7b9c1d3",
    ),
)
```

## Environments

This SDK allows you to configure different environments for API requests.

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from fern import AsyncFernApi

client = AsyncFernApi(
    token="<token>",
)


async def main() -> None:
    await client.clusters.create_cluster(
        name="tenant-a-prod",
        control_plane_kubernetes_version="1.33.4",
        etcd_encrypted=True,
        network=ClusterNetworkCreateConfig(
            pod_cidr="192.168.0.0/16",
            service_cidr="10.96.0.0/12",
        ),
        node_pools=[
            NodePoolCreateConfig(
                name="gpu-workers",
                node_name_prefix="w",
                system_reserved_memory="16Gi",
                node_labels={
                    "nvidia.com/gpu.present": "true"
                },
                node_taints=[
                    NodeTaint(
                        key="nvidia.com/dedicated",
                        value="gpu",
                        effect=NodeTaintEffect.NO_SCHEDULE,
                    )
                ],
                desired_node_count=2,
                recycle_budget=1,
                nico=NicoNodePoolProvider(
                    vpc_prefix_i_ds=[
                        "2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"
                    ],
                    instance_type_id="0d2f4a6c-8e0b-4d2f-9a4c-6e8b0d2f4a6c",
                    ssh_key_group_i_ds=[
                        "3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"
                    ],
                    release="example-ubuntu-24.04-amd64",
                ),
            )
        ],
        control_plane_config=CreateClusterControlPlaneConfig(
            desired_count=3,
            max_surge=1,
            system_reserved_memory="16Gi",
            nico=NicoControlPlaneProviderCreate(
                instance_type_preference=[
                    "1c3e5a7f-9b1d-4f3e-a5c7-e9b1d3f5a7c9"
                ],
                vpc_prefix_i_ds=[
                    "2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"
                ],
                release="example-ubuntu-24.04-amd64",
                ssh_key_group_i_ds=[
                    "3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"
                ],
            ),
        ),
        nico=NicoClusterProvider(
            org_id="dipfedrcvjiw",
            site_id="4f6a8c2e-1b3d-4e5f-a7b9-c1d3e5f7a9b1",
            vpc_id="6a8c0e4f-3d5b-4f7a-b9c1-e3f5a7b9c1d3",
        ),
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from fern.core.api_error import ApiError

try:
    client.clusters.create_cluster(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from fern import FernApi

client = FernApi(...)
response = client.clusters.with_raw_response.create_cluster(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.clusters.create_cluster(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from fern import FernApi

client = FernApi(..., timeout=20.0)

# Override timeout for a specific method
client.clusters.create_cluster(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from fern import FernApi

client = FernApi(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
