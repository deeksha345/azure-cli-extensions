# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "connectedmachine private-link-scope update",
)
class Update(AAZCommand):
    """Update an Azure Arc PrivateLinkScope. Note: You cannot                                          specify a different value for InstrumentationKey nor AppId in the Put operation.

    :example: Sample command for private-link-scope update
        az connectedmachine private-link-scope update --location westus --tags Tag1=Value1 --resource-group my-resource-group --scope-name my-privatelinkscope
    """

    _aaz_info = {
        "version": "2024-05-20-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.hybridcompute/privatelinkscopes/{}", "2024-05-20-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.scope_name = AAZStrArg(
            options=["-n", "--name", "--scope-name"],
            help="The name of the Azure Arc PrivateLinkScope resource.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="[a-zA-Z0-9-_\.]+",
            ),
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.public_network_access = AAZStrArg(
            options=["--public-network-access"],
            arg_group="Properties",
            help="Indicates whether machines associated with the private link scope can also use public Azure Arc service endpoints.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled", "SecuredByPerimeter": "SecuredByPerimeter"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PrivateLinkScopesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.PrivateLinkScopesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PrivateLinkScopesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/privateLinkScopes/{scopeName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "scopeName", self.ctx.args.scope_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-05-20-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_hybrid_compute_private_link_scope_read(cls._schema_on_200)

            return cls._schema_on_200

    class PrivateLinkScopesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/privateLinkScopes/{scopeName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "scopeName", self.ctx.args.scope_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-05-20-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_hybrid_compute_private_link_scope_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("publicNetworkAccess", AAZStrType, ".public_network_access")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_hybrid_compute_private_link_scope_read = None

    @classmethod
    def _build_schema_hybrid_compute_private_link_scope_read(cls, _schema):
        if cls._schema_hybrid_compute_private_link_scope_read is not None:
            _schema.id = cls._schema_hybrid_compute_private_link_scope_read.id
            _schema.location = cls._schema_hybrid_compute_private_link_scope_read.location
            _schema.name = cls._schema_hybrid_compute_private_link_scope_read.name
            _schema.properties = cls._schema_hybrid_compute_private_link_scope_read.properties
            _schema.system_data = cls._schema_hybrid_compute_private_link_scope_read.system_data
            _schema.tags = cls._schema_hybrid_compute_private_link_scope_read.tags
            _schema.type = cls._schema_hybrid_compute_private_link_scope_read.type
            return

        cls._schema_hybrid_compute_private_link_scope_read = _schema_hybrid_compute_private_link_scope_read = AAZObjectType()

        hybrid_compute_private_link_scope_read = _schema_hybrid_compute_private_link_scope_read
        hybrid_compute_private_link_scope_read.id = AAZStrType(
            flags={"read_only": True},
        )
        hybrid_compute_private_link_scope_read.location = AAZStrType(
            flags={"required": True},
        )
        hybrid_compute_private_link_scope_read.name = AAZStrType(
            flags={"read_only": True},
        )
        hybrid_compute_private_link_scope_read.properties = AAZObjectType()
        hybrid_compute_private_link_scope_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        hybrid_compute_private_link_scope_read.tags = AAZDictType()
        hybrid_compute_private_link_scope_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_hybrid_compute_private_link_scope_read.properties
        properties.private_endpoint_connections = AAZListType(
            serialized_name="privateEndpointConnections",
            flags={"read_only": True},
        )
        properties.private_link_scope_id = AAZStrType(
            serialized_name="privateLinkScopeId",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_network_access = AAZStrType(
            serialized_name="publicNetworkAccess",
        )

        private_endpoint_connections = _schema_hybrid_compute_private_link_scope_read.properties.private_endpoint_connections
        private_endpoint_connections.Element = AAZObjectType()

        _element = _schema_hybrid_compute_private_link_scope_read.properties.private_endpoint_connections.Element
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType()
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_hybrid_compute_private_link_scope_read.properties.private_endpoint_connections.Element.properties
        properties.group_ids = AAZListType(
            serialized_name="groupIds",
            flags={"read_only": True},
        )
        properties.private_endpoint = AAZObjectType(
            serialized_name="privateEndpoint",
        )
        properties.private_link_service_connection_state = AAZObjectType(
            serialized_name="privateLinkServiceConnectionState",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        group_ids = _schema_hybrid_compute_private_link_scope_read.properties.private_endpoint_connections.Element.properties.group_ids
        group_ids.Element = AAZStrType()

        private_endpoint = _schema_hybrid_compute_private_link_scope_read.properties.private_endpoint_connections.Element.properties.private_endpoint
        private_endpoint.id = AAZStrType()

        private_link_service_connection_state = _schema_hybrid_compute_private_link_scope_read.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
        private_link_service_connection_state.actions_required = AAZStrType(
            serialized_name="actionsRequired",
            flags={"read_only": True},
        )
        private_link_service_connection_state.description = AAZStrType(
            flags={"required": True},
        )
        private_link_service_connection_state.status = AAZStrType(
            flags={"required": True},
        )

        system_data = _schema_hybrid_compute_private_link_scope_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_hybrid_compute_private_link_scope_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_hybrid_compute_private_link_scope_read.id
        _schema.location = cls._schema_hybrid_compute_private_link_scope_read.location
        _schema.name = cls._schema_hybrid_compute_private_link_scope_read.name
        _schema.properties = cls._schema_hybrid_compute_private_link_scope_read.properties
        _schema.system_data = cls._schema_hybrid_compute_private_link_scope_read.system_data
        _schema.tags = cls._schema_hybrid_compute_private_link_scope_read.tags
        _schema.type = cls._schema_hybrid_compute_private_link_scope_read.type


__all__ = ["Update"]
