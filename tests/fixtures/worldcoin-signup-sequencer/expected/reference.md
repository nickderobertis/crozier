# Reference
## Identities
<details><summary><code>client.identities.<a href="src/fern/identities/client.py">add_new_identity_to_the_queue</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new identity commitment to the sequencer queue.
V3 differs from V2 in that it allows re-adding deleted identities.
If the identity was previously deleted and the leaf index contains Hash::ZERO,
it can be re-added.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.identities.add_new_identity_to_the_queue(
    commitment="commitment",
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

**commitment:** `str` — Identity commitment
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">add_identity_removal_to_the_queue</a>(...)</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.identities.add_identity_removal_to_the_queue(
    commitment="commitment",
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

**commitment:** `str` — Identity commitment
    
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

<details><summary><code>client.identities.<a href="src/fern/identities/client.py">get_inclusion_proof_of_identity_by_proof_type</a>(...) -> InclusionProof</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns inclusion proof for the specified identity at different stages:
- `processed`: Proof from the processed tree (latest committed batch)
- `mined`: Proof from the mined tree (on-chain confirmed)
- `bridged`: Proof from the bridged tree (cross-chain confirmed)
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
from fern.identities import GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.identities.get_inclusion_proof_of_identity_by_proof_type(
    commitment="commitment",
    inclusion_proof_type=GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType.PROCESSED,
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

**commitment:** `str` — Identity commitment
    
</dd>
</dl>

<dl>
<dd>

**inclusion_proof_type:** `GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType` — Type of inclusion proof to retrieve
    
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

## SemaphoreProof
<details><summary><code>client.semaphore_proof.<a href="src/fern/semaphore_proof/client.py">verify_semaphore_proof</a>(...) -> SemaphoreProofVerificationResult</code></summary>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.semaphore_proof.verify_semaphore_proof(
    root="0x00000abbda2bb9080713c20975bd1b711ebcd413e52a2a5d4c1d6114cb179b0f",
    signal_hash="0x000041b9e22987d04f56445733b5b351693afd82f0584e3442de71adfcd408ca",
    nullifier_hash="0x000012e8498adcc7a2e04ac3c4ef82ee13db7a710a7174b9623fdb8c8ccd38fd",
    external_nullifier_hash="0x000003282d8e4502363cf69bf7d236bd777b8aab7a232bb96b1a17ec2bbb029a",
    proof=[
        ["0x000012bab4c2b8ee80203b053f7edd25408ce4898f9ee48cd1cf5fa05b382258", "0x0000ffed4784db6fd39228c98015be3332bf594460340301dd02e05ccad3a7e5"],
        [["0x0000ba984420b405e2102ec8a3f991d207ae29b65804d4b9ab41f752fcd6f9b0", "0x000072d536482dd3f680a869050426cb0230b0aaf999b89206848406c6b070ac"], ["0x000059f64d1f40212a4be836ec09c1bc675b3315e2f0a6343f7c3c96dac99941", "0x0000ea95958f6182420c86be4e1507f640d77ba9f377bbf3025ff196067411a3"]],
        ["0x00007c66ab60056f9e021d55f98ea3e6e9ce8db0ef5ca3af6b2c8db1b3018425", "0x0000c0eb8ef9f315815947adce6ed324f49b58a544a37a77185eab9a7202ca1b"]
    ],
    max_root_age_seconds=3600,
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

**root:** `FieldElement` 
    
</dd>
</dl>

<dl>
<dd>

**signal_hash:** `FieldElement` 
    
</dd>
</dl>

<dl>
<dd>

**nullifier_hash:** `FieldElement` 
    
</dd>
</dl>

<dl>
<dd>

**external_nullifier_hash:** `FieldElement` 
    
</dd>
</dl>

<dl>
<dd>

**proof:** `SemaphoreProof` 
    
</dd>
</dl>

<dl>
<dd>

**max_root_age_seconds:** `typing.Optional[int]` — Maximum age of the root in seconds
    
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

