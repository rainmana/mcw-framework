# MCW Framework — Diagrams

Visual representations of the core framework constructs. All diagrams are defined as source text (Mermaid) and version-controlled alongside the framework documentation.

---

## Diagram 1: The Three Context Windows

This diagram shows the relationship between the Human Context Window (HCW), the Artificial Context Window (ACW), and the Meta-Context Window (MCW) that emerges between them through IU exchange.

MCW is not contained in either party — it exists only in the space created by active, bidirectional exchange.

```mermaid
graph LR
    subgraph HCW["HCW — Human Context Window"]
        H1["Working memory"]
        H2["Intent & goals"]
        H3["Unspoken assumptions"]
        H4["Salience weighting"]
        H5["Advances between turns"]
    end

    subgraph MCW["MCW — Meta-Context Window  (emergent)"]
        direction TB
        M1["Shared coordination state"]
        M2["Bidirectional · Temporal · Lossy · Repairable"]
    end

    subgraph ACW["ACW — Artificial Context Window"]
        A1["Tokens & embeddings"]
        A2["Retrieved IUs (RAG)"]
        A3["Attention patterns"]
        A4["Updates on input only"]
    end

    HCW <-->|"IU exchange\n(text, speech, symbols)"| MCW
    MCW <-->|"IU exchange\n(tokens, probabilities)"| ACW
```

**Key observations:**
- MCW does not exist independently — it arises from the exchange
- The HCW advances continuously; the ACW advances only when input arrives
- The exchange channel is constrained by bandwidth, latency, and modality (C in the coupling function)

---

## Diagram 2: IU Flow Model

Information Units travel through five stages during any communicative act. MCW health is determined by cumulative fidelity across all five stages. Failure at any stage contributes to MCW entropy.

```mermaid
flowchart LR
    S1(["1 · Selection"])
    S2(["2 · Encoding"])
    S3(["3 · Transmission"])
    S4(["4 · Decoding"])
    S5(["5 · Integration"])

    S1 -->|"IU chosen\nfor transfer"| S2
    S2 -->|"Compressed into\nlanguage / tokens"| S3
    S3 -->|"Through constrained\nchannel"| S4
    S4 -->|"Reconstructed via\nprior context"| S5

    F1["⚠ Omission\nSalience mismatch\nSelf-censorship"]
    F2["⚠ Overcompression\nAmbiguity introduced"]
    F3["⚠ Noise · Latency\nBandwidth limits"]
    F4["⚠ Misinterpretation\nAssumption error"]
    F5["⚠ Drift\nWeighting mismatch"]

    S1 -. failure .-> F1
    S2 -. failure .-> F2
    S3 -. failure .-> F3
    S4 -. failure .-> F4
    S5 -. failure .-> F5
```

**Transmission (Stage 3) is highlighted** because it is the stage most constrained by channel properties (C in the coupling function) and the least within either actor's control.

---

## Diagram 3: MCW Failure Taxonomy

The six MCW failure modes, organized by the stage of the IU flow model where they primarily originate and whether they affect primarily the HCW side, the ACW side, or the channel between them.

```mermaid
mindmap
  root(("MCW\nDegradation"))
    Selection failures
      Asymmetric State Advancement
        Human advances HCW off-turn
        ACW not updated
        Phase lag accumulates
      Repair Suppression
        Clarification discouraged
        Immune signals blocked
        Drift accelerates
    Encoding / Decoding failures
      Overcompression
        Premature summarization
        IU distinctions lost
        Edge cases vanish
      False Alignment
        Shared language
        Divergent meaning
        Agreement inferred not verified
    Channel / Hidden variable failures
      Constraint Opacity
        Hidden system-prompt IUs
        Policy restrictions invisible
        Repair misdirected
      Drift
        Silent desynchronization
        Assumptions accumulate
        Priorities shift implicitly
```

---

## Diagram 4: MCW Repair Flow

How a degraded MCW is identified and repaired. Each repair operation corresponds to a specific failure mode. Repair must happen before progress — pushing through a degraded MCW compounds entropy.

```mermaid
flowchart TD
    A([Interaction in progress]) --> B{MCW vitals check}

    B -->|"H high · R low\nD low · M low"| C([Continue · MCW healthy])
    B -->|"Signal detected"| D[Name the failure mode]

    D --> E{Which failure mode?}

    E -->|Drift| F["Re-grounding\nRestate goals & assumptions"]
    E -->|"Asymmetric\nadvancement"| G["Synchronization\nExternalize off-turn state"]
    E -->|"False alignment"| H["Disambiguation\nSplit overloaded IUs"]
    E -->|Overcompression| I["Decompression\nExpand summary back out"]
    E -->|"Constraint opacity"| J["Re-weighting\nMake constraints visible"]
    E -->|"Repair suppression"| K["Repair permission\nExplicitly authorize signals"]

    F --> L{MCW restored?}
    G --> L
    H --> L
    I --> L
    J --> L
    K --> L

    L -->|Yes| C
    L -->|No| M["Escalate repair\nRe-ground from scratch\nor reset with HCW briefing"]
    M --> B
```

**Critical rule:** Repair must happen *before* resuming progress. Each turn of forward motion on a degraded MCW deepens the entropy — making later repair exponentially more expensive.

---

## Diagram 5: OSI Layers of Understanding

The framework's layered accessibility model. The same constructs appear at each layer; only the compression level changes. No concept appears at a higher layer unless it already exists at a lower layer.

```mermaid
graph TD
    L0["Layer 0 · Intuition\nAnyone\nAre we on the same page?"]
    L1["Layer 1 · Concepts\nGeneralists\nMCW as shared coordination state\nIUs as coordination atoms"]
    L2["Layer 2 · Formalization\nSTEM-adjacent\nEntropy · IU flow model · Coupling function"]
    L3["Layer 3 · Models\nResearchers\nEntropy flows · Phase transitions · Drift metrics"]
    L4["Layer 4 · Implementation\nBuilders\nTest beds · Simulations · Experiment protocols"]
    L5["Layer 5 · Application\nDomain specialists\nBiology · Organizations · AI · Policy"]

    L0 --> L1 --> L2 --> L3 --> L4 --> L5

    R["Invariant rule:\nNo concept appears at layer N\nunless it exists at layer N-1\nin compressed form"]

    L2 -. governs .-> R
```

---

*All diagrams are defined as Mermaid source in [`docs/diagrams.md`](https://github.com/rainmana/mcw-framework/blob/main/docs/diagrams.md) and render in the browser. They can be updated by editing the source directly in the repository.*
