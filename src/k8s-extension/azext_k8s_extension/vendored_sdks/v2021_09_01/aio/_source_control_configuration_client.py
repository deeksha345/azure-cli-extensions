# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

<<<<<<< HEAD
from copy import deepcopy
from typing import Any, Awaitable, Optional, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from .. import models
from ._configuration import SourceControlConfigurationClientConfiguration
from .operations import ExtensionsOperations, OperationStatusOperations, Operations

=======
from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

>>>>>>> 331f997c (updating to the latest vendored sdk)
if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

<<<<<<< HEAD
class SourceControlConfigurationClient:
    """KubernetesConfiguration Client.

    :ivar extensions: ExtensionsOperations operations
    :vartype extensions:
     azure.mgmt.kubernetesconfiguration.v2021_09_01.aio.operations.ExtensionsOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status:
     azure.mgmt.kubernetesconfiguration.v2021_09_01.aio.operations.OperationStatusOperations
=======
from ._configuration import SourceControlConfigurationClientConfiguration
from .operations import ExtensionsOperations
from .operations import OperationStatusOperations
from .operations import Operations
from .. import models


class SourceControlConfigurationClient(object):
    """KubernetesConfiguration Client.

    :ivar extensions: ExtensionsOperations operations
    :vartype extensions: azure.mgmt.kubernetesconfiguration.v2021_09_01.aio.operations.ExtensionsOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status: azure.mgmt.kubernetesconfiguration.v2021_09_01.aio.operations.OperationStatusOperations
>>>>>>> 331f997c (updating to the latest vendored sdk)
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.kubernetesconfiguration.v2021_09_01.aio.operations.Operations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
<<<<<<< HEAD
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
=======
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
>>>>>>> 331f997c (updating to the latest vendored sdk)
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
<<<<<<< HEAD
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = SourceControlConfigurationClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
=======
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SourceControlConfigurationClientConfiguration(credential, subscription_id, **kwargs)
>>>>>>> 331f997c (updating to the latest vendored sdk)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
<<<<<<< HEAD
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.extensions = ExtensionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operation_status = OperationStatusOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)
=======
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.extensions = ExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response
>>>>>>> 331f997c (updating to the latest vendored sdk)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SourceControlConfigurationClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
