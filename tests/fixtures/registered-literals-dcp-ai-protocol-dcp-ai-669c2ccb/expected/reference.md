# Reference
## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py#L26-L49">check</a>() -> HealthCheckResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.health.check()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Discovery
<details><summary><code>client.discovery.<a href="src/fern/discovery/client.py#L26-L51">get_capabilities</a>() -> DcpCapabilities</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns supported DCP versions, algorithms, wire formats, and feature flags.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.discovery.get_capabilities()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Advisory
<details><summary><code>client.advisory.<a href="src/fern/advisory/client.py#L33-L58">get_algorithm_advisories</a>() -> GetAlgorithmAdvisoriesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.advisory.get_algorithm_advisories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.advisory.<a href="src/fern/advisory/client.py#L60-L101">publish_advisory</a>(...) -> PublishAdvisoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes a governance-signed algorithm advisory (deprecate/warn/revoke).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AlgorithmAdvisory, AlgorithmAdvisoryType, AlgorithmAdvisoryAction
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.advisory.publish_advisory(
    advisory=AlgorithmAdvisory(
        type=AlgorithmAdvisoryType.ALGORITHM_ADVISORY,
        advisory_id="advisory_id",
        affected_algorithms=[
            "affected_algorithms"
        ],
        action=AlgorithmAdvisoryAction.DEPRECATE,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**advisory:** `AlgorithmAdvisory` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.advisory.<a href="src/fern/advisory/client.py#L103-L126">check_advisories</a>() -> CheckAdvisoriesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.advisory.check_advisories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.advisory.<a href="src/fern/advisory/client.py#L128-L157">auto_apply_advisories</a>() -> AutoApplyAdvisoriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scans active advisories and automatically updates the verifier policy
by removing deprecated/revoked algorithms and adding replacements.
May auto-switch to pq_only mode if all classical algorithms are removed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.advisory.auto_apply_advisories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Governance
<details><summary><code>client.governance.<a href="src/fern/governance/client.py#L30-L53">get_governance_keys</a>() -> GovernanceKeySet</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.governance.get_governance_keys()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.<a href="src/fern/governance/client.py#L55-L90">register_governance</a>(...) -> RegisterGovernanceResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GovernanceKeySet, KeyEntryV2
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.governance.register_governance(
    governance_key_set=GovernanceKeySet(
        governance_id="governance_id",
        keys=[
            KeyEntryV2()
        ],
        threshold=1,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**governance_key_set:** `GovernanceKeySet` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Verification
<details><summary><code>client.verification.<a href="src/fern/verification/client.py#L32-L135">verify_bundle</a>(...) -> VerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs full DCP verification with automatic version detection:

V1: Schema validation, Ed25519 signature, bundle hash integrity,
Merkle root, intent hash chain, and previous hash chain verification.

V2: Composite signature structure, session nonce consistency,
manifest integrity, tier-aware policy enforcement.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SignedBundleV2, CitizenshipBundleV2, CitizenshipBundleV2DcpBundleVersion, BundleManifest, SignedPayload, CompositeSignature, SignedBundleV2Signature, CompositeSignatureClassical, CompositeSignaturePq, CompositeSignatureBinding
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.verification.verify_bundle(
    signed_bundle=SignedBundleV2(
        bundle=CitizenshipBundleV2(
            dcp_bundle_version=CitizenshipBundleV2DcpBundleVersion.TWO0,
            manifest=BundleManifest(
                session_nonce="a1b2c3...",
                rpr_hash="sha256:...",
                passport_hash="sha256:...",
                intent_hash="sha256:...",
                policy_hash="sha256:...",
                audit_merkle_root="sha256:...",
                audit_count=1,
            ),
            responsible_principal_record=SignedPayload(
                payload={
                    "key": "value"
                },
                composite_sig=CompositeSignature(),
            ),
            agent_passport=SignedPayload(
                payload={
                    "key": "value"
                },
                composite_sig=CompositeSignature(),
            ),
            intent=SignedPayload(
                payload={
                    "key": "value"
                },
                composite_sig=CompositeSignature(),
            ),
            policy_decision=SignedPayload(
                payload={
                    "key": "value"
                },
                composite_sig=CompositeSignature(),
            ),
            audit_entries=[
                {
                    "key": "value"
                }
            ],
        ),
        signature=SignedBundleV2Signature(
            composite_sig=CompositeSignature(
                classical=CompositeSignatureClassical(
                    alg="ed25519",
                    kid="abc123",
                    sig_b64="...",
                ),
                pq=CompositeSignaturePq(
                    alg="ml-dsa-65",
                    kid="def456",
                    sig_b64="...",
                ),
                binding=CompositeSignatureBinding.PQ_OVER_CLASSICAL,
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**signed_bundle:** `VerifyBundleRequestSignedBundle` 
    
</dd>
</dl>

<dl>
<dd>

**public_key_b64:** `typing.Optional[str]` — Optional Ed25519 public key (base64) for V1. Falls back to signer.public_key_b64.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verification.<a href="src/fern/verification/client.py#L137-L170">verify_bundle_v2</a>(...) -> VerifyBundleV2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs tier-aware V2 bundle verification including composite signature
validation, session binding, manifest integrity, and security tier enforcement.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.verification.verify_bundle_v2()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**signed_bundle:** `typing.Optional[SignedBundleV2]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Anchoring
<details><summary><code>client.anchoring.<a href="src/fern/anchoring/client.py#L30-L71">anchor_hash</a>(...) -> AnchorReceipt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Anchors a bundle hash (or batch of hashes) to an L2 blockchain.
Returns 501 on the reference gateway; use the anchor service (port 3001) directly.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.anchoring import AnchorHashRequestChain

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.anchoring.anchor_hash(
    bundle_hash="sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    chain=AnchorHashRequestChain.BASE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bundle_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[AnchorHashRequestChain]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Revocation
<details><summary><code>client.revocation.<a href="src/fern/revocation/client.py#L32-L57">list_revocations</a>() -> ListRevocationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Available on the revocation service (port 3003).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.revocation.list_revocations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.revocation.<a href="src/fern/revocation/client.py#L59-L125">publish_revocation</a>(...) -> PublishRevocationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Available on the revocation service (port 3003).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.revocation.publish_revocation(
    dcp_version="dcp_version",
    agent_id="agent_id",
    human_id="human_id",
    timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    reason="reason",
    signature="signature",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RevocationRecord` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.revocation.<a href="src/fern/revocation/client.py#L127-L158">check_revocation</a>(...) -> CheckRevocationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Available on the revocation service (port 3003).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.revocation.check_revocation(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transparency
<details><summary><code>client.transparency.<a href="src/fern/transparency/client.py#L36-L67">add_to_log</a>(...) -> AddToLogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Available on the transparency-log service (port 3002).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transparency.add_to_log(
    bundle_hash="bundle_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bundle_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transparency.<a href="src/fern/transparency/client.py#L69-L94">get_log_root</a>() -> GetLogRootResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Available on the transparency-log service (port 3002).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transparency.get_log_root()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transparency.<a href="src/fern/transparency/client.py#L96-L125">get_log_proof</a>(...) -> InclusionProof</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Available on the transparency-log service (port 3002).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transparency.get_log_proof(
    index=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**index:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transparency.<a href="src/fern/transparency/client.py#L127-L153">get_signed_tree_head</a>() -> SignedTreeHead</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a Signed Tree Head — the current Merkle root signed by the log operator.
Used for gossip protocol cross-log verification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transparency.get_signed_tree_head()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transparency.<a href="src/fern/transparency/client.py#L155-L180">get_gossip_peers</a>() -> GetGossipPeersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all known gossip peers and recent split-view alerts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transparency.get_gossip_peers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transparency.<a href="src/fern/transparency/client.py#L182-L216">add_gossip_peer</a>(...) -> AddGossipPeerResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transparency.add_gossip_peer(
    peer_id="peer_id",
    endpoint="endpoint",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**peer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transparency.<a href="src/fern/transparency/client.py#L218-L248">gossip_exchange</a>(...) -> GossipExchangeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange signed tree heads between log instances for cross-verification.
Detects split-view attacks when roots differ for the same tree size.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transparency.gossip_exchange()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sth:** `typing.Optional[SignedTreeHead]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transparency.<a href="src/fern/transparency/client.py#L250-L273">get_gossip_alerts</a>() -> GetGossipAlertsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transparency.get_gossip_alerts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Passport
<details><summary><code>client.passport.<a href="src/fern/passport/client.py#L30-L93">register_passport</a>(...) -> RegisterPassportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a V2 agent passport with composite-signed keys.
Verifies deterministic kid derivation and stores keys in the registry.
Optionally registers an emergency revocation token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SignedPayload, CompositeSignature, CompositeSignatureClassical, CompositeSignatureBinding
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.passport.register_passport(
    signed_passport=SignedPayload(
        payload={
            "dcp_version": "2.0",
            "agent_id": "agent-001",
            "session_nonce": "a1b2c3d4...",
            "keys": [{"kid": "abc123...", "alg": "ed25519", "public_key_b64": "...", "created_at": "2026-03-01T00:00:00Z", "status": "active"}],
            "emergency_revocation_token": "sha256:..."
        },
        composite_sig=CompositeSignature(
            classical=CompositeSignatureClassical(
                alg="ed25519",
                kid="abc123",
                sig_b64="...",
            ),
            binding=CompositeSignatureBinding.CLASSICAL_ONLY,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**signed_passport:** `SignedPayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Intent
<details><summary><code>client.intent.<a href="src/fern/intent/client.py#L30-L85">declare_intent</a>(...) -> DeclareIntentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits a signed intent declaration. The server computes a risk score,
security tier, and policy decision (approve/escalate/block).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SignedPayload, CompositeSignature, CompositeSignatureClassical, CompositeSignatureBinding
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.intent.declare_intent(
    signed_intent=SignedPayload(
        payload={
            "dcp_version": "2.0",
            "intent_id": "intent-001",
            "agent_id": "agent-001",
            "session_nonce": "a1b2c3d4...",
            "action_type": "api_call",
            "estimated_impact": "low"
        },
        composite_sig=CompositeSignature(
            classical=CompositeSignatureClassical(
                alg="ed25519",
                kid="abc123",
                sig_b64="...",
            ),
            binding=CompositeSignatureBinding.CLASSICAL_ONLY,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**signed_intent:** `SignedPayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Audit
<details><summary><code>client.audit.<a href="src/fern/audit/client.py#L31-L70">append_audit</a>(...) -> AppendAuditResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Appends a signed audit event to the agent's audit chain, verifying prev_hash continuity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.audit.append_audit(
    audit_event={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audit_event:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audit.<a href="src/fern/audit/client.py#L72-L114">compact_audit</a>(...) -> CompactAuditResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an audit compaction with a Merkle root covering a range of events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CompositeSignature
from fern.environment import FernApiEnvironment
from fern.audit import CompactAuditRequestCompaction, CompactAuditRequestCompactionType

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.audit.compact_audit(
    compaction=CompactAuditRequestCompaction(
        type=CompactAuditRequestCompactionType.AUDIT_COMPACTION,
        session_nonce="session_nonce",
        range={
            "key": "value"
        },
        merkle_root="merkle_root",
        composite_sig=CompositeSignature(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**compaction:** `CompactAuditRequestCompaction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Keys
<details><summary><code>client.keys.<a href="src/fern/keys/client.py#L31-L58">lookup_key</a>(...) -> LookupKeyResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.keys.lookup_key(
    kid="kid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.keys.<a href="src/fern/keys/client.py#L60-L109">rotate_key</a>(...) -> RotateKeyResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, KeyEntryV2
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.keys.rotate_key(
    old_kid="old_kid",
    new_key=KeyEntryV2(),
    proof_of_possession={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**old_kid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**new_key:** `KeyEntryV2` 
    
</dd>
</dl>

<dl>
<dd>

**proof_of_possession:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization_sig:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Emergency
<details><summary><code>client.emergency.<a href="src/fern/emergency/client.py#L29-L73">revoke</a>(...) -> EmergencyRevokeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes all keys for an agent using a pre-registered emergency revocation
secret. Rate-limited to 5 requests per minute per IP.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.emergency.revoke(
    agent_id="agent-001",
    revocation_secret="a1b2c3d4e5f6...",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**revocation_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**human_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## MultiParty
<details><summary><code>client.multi_party.<a href="src/fern/multi_party/client.py#L30-L78">multi_party_authorize</a>(...) -> MultiPartyAuthorizeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a multi-party authorization request. Requires at least the
threshold number of authorizations including an owner signature.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.multi_party import MultiPartyAuthorizeRequestAuthorization, MultiPartyAuthorizeRequestAuthorizationType, MultiPartyAuthorizeRequestAuthorizationOperation, MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.multi_party.multi_party_authorize(
    authorization=MultiPartyAuthorizeRequestAuthorization(
        type=MultiPartyAuthorizeRequestAuthorizationType.MULTI_PARTY_AUTHORIZATION,
        operation=MultiPartyAuthorizeRequestAuthorizationOperation.REVOKE_AGENT,
        authorizations=[
            MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem()
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `MultiPartyAuthorizeRequestAuthorization` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Policy
<details><summary><code>client.policy.<a href="src/fern/policy/client.py#L31-L54">get_policy</a>() -> GetPolicyResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.policy.get_policy()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.policy.<a href="src/fern/policy/client.py#L56-L87">switch_policy_mode</a>(...) -> SwitchPolicyModeResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.policy import SwitchPolicyModeRequestMode

client = FernApi(
    token="<token>",
    dcp_api_key="<X-DCP-API-Key>",
    environment=FernApiEnvironment.DEFAULT,
)

client.policy.switch_policy_mode(
    mode=SwitchPolicyModeRequestMode.HYBRID_REQUIRED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mode:** `SwitchPolicyModeRequestMode` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

