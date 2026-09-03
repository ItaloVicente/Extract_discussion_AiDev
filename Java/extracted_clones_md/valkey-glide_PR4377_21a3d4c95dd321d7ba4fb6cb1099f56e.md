# 🔍 Clone Analysis | Project: valkey-glide | PR: #4377

- **Commit SHA:** `cd8de5d4c36cc43717e04bc92eea06f8d060d3ac`
- **Clone Fingerprint:** `21a3d4c95dd321d7ba4fb6cb1099f56e`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `java/client/src/main/java/glide/managers/ConnectionManager.java`
**Lines:** 173 to 205

```text
private ConnectionRequest.Builder setupConnectionRequestBuilderGlideClient(
            GlideClientConfiguration configuration) {
        ConnectionRequest.Builder connectionRequestBuilder =
                setupConnectionRequestBuilderBaseConfiguration(configuration);
        connectionRequestBuilder.setClusterModeEnabled(false);

        if (configuration.getDatabaseId() != null) {
            connectionRequestBuilder.setDatabaseId(configuration.getDatabaseId());
        }

        if (configuration.getSubscriptionConfiguration() != null) {
            if (configuration.getProtocol() == ProtocolVersion.RESP2) {
                throw new ConfigurationError(
                        "PubSub subscriptions require RESP3 protocol, but RESP2 was configured.");
            }
            var subscriptionsBuilder = PubSubSubscriptions.newBuilder();
            for (var entry : configuration.getSubscriptionConfiguration().getSubscriptions().entrySet()) {
                var channelsBuilder = PubSubChannelsOrPatterns.newBuilder();
                for (var channel : entry.getValue()) {
                    channelsBuilder.addChannelsOrPatterns(ByteString.copyFrom(channel.getBytes()));
                }
                subscriptionsBuilder.putChannelsOrPatternsByType(
                        entry.getKey().ordinal(), channelsBuilder.build());
            }
            connectionRequestBuilder.setPubsubSubscriptions(subscriptionsBuilder.build());
        }

        connectionRequestBuilder =
                setupConnectionRequestBuilderAdvancedBaseConfiguration(
                        connectionRequestBuilder, configuration.getAdvancedConfiguration());

        return connectionRequestBuilder;
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `java/client/src/main/java/glide/managers/ConnectionManager.java`
**Lines:** 240 to 268

```text
private ConnectionRequest.Builder setupConnectionRequestBuilderGlideClusterClient(
            GlideClusterClientConfiguration configuration) {
        ConnectionRequest.Builder connectionRequestBuilder =
                setupConnectionRequestBuilderBaseConfiguration(configuration);
        connectionRequestBuilder.setClusterModeEnabled(true);

        if (configuration.getSubscriptionConfiguration() != null) {
            if (configuration.getProtocol() == ProtocolVersion.RESP2) {
                throw new ConfigurationError(
                        "PubSub subscriptions require RESP3 protocol, but RESP2 was configured.");
            }
            var subscriptionsBuilder = PubSubSubscriptions.newBuilder();
            for (var entry : configuration.getSubscriptionConfiguration().getSubscriptions().entrySet()) {
                var channelsBuilder = PubSubChannelsOrPatterns.newBuilder();
                for (var channel : entry.getValue()) {
                    channelsBuilder.addChannelsOrPatterns(ByteString.copyFrom(channel.getBytes()));
                }
                subscriptionsBuilder.putChannelsOrPatternsByType(
                        entry.getKey().ordinal(), channelsBuilder.build());
            }
            connectionRequestBuilder.setPubsubSubscriptions(subscriptionsBuilder.build());
        }

        connectionRequestBuilder =
                setupConnectionRequestBuilderAdvancedBaseConfiguration(
                        connectionRequestBuilder, configuration.getAdvancedConfiguration());

        return connectionRequestBuilder;
    }
```

