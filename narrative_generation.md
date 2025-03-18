# Narrative Generation from Screenshots using OLCA + Vision AI

## Objective:
Enable OLCA to process screenshots through an integrated vision-based model (Ollama) and generate structured narratives. This extends OLCA’s utility from CLI session tracking to context-aware storytelling, creating metadata-rich logs of user interactions.

## Feature Scope

### 1. Screenshot Capture & Processing
**What This Enables:**
- OLCA detects and processes captured screenshots.
- Uses Ollama Vision Model for image interpretation & contextual classification.
- Extracted data is structured into a narrative format.

**Implementation Details:**
- Monitor system screenshot events.
- Extract metadata (timestamp, application state, UI elements).
- Send data to Ollama Vision Model for interpretation.
- Output structured text in `OLCA_Narratives/`.

**Example Use Case:**
```sh
> screenshot.png detected
> olca-analyze screenshot.png
```
**Narrative Generated in `OLCA_Narratives/`**
```json
{
  "timestamp": "2025-03-14T14:32:00Z",
  "scene": "Ubuntu Notification Settings",
  "options": ["Run Command", "Log to File", "Speak Text"],
  "context": "User decision process in notification configuration",
  "story": "The screen hummed with potential, awaiting the user's next move."
}
```

### 2. Adaptive Narrative Structuring
**What This Enables:**
- Converts system interactions into recursive narratives.
- Detects patterns in screenshots to connect sequential events.
- Generates multi-act structures based on interactions.

**Implementation Details:**
- Identify common UI states across screenshots.
- Apply a three-act structure for event chains.
- Detect unique residual markers (e.g., persistent UI elements or anomalies).

**Example Use Case:**
```sh
> olca-narrative --track-session
```
**OLCA Detects a Recurring Pattern & Expands the Story**
```json
{
  "narrative_structure": "recursive",
  "ontology_expansion": true,
  "trace_structuring": true,
  "annotations": "Unfolding recursion detected. The past adapts into the present."
}
```

### 3. System-State Aware Storytelling
**What This Enables:**
- Embeds system activity into generated stories.
- Detects user workflow trends and annotates deviations.
- Creates a self-reflective system narrative.

**Implementation Details:**
- Store system context within `OLCA_Narratives/`.
- Identify points of recursion in user workflows.
- Generate dynamic annotations based on system state.

**Example Use Case:**
```sh
> olca-narrative --review-session
```
**Narrative-Driven Debugging & Exploration**
```json
{
  "system_state": "recursive",
  "persistent_markers": "Handprint signature detected in workflow",
  "story": "A message embedded in the architecture, repeating across sessions."
}
```

## Suggested Development Plan

**Step 1: Implement Screenshot Parsing with Ollama Vision**
- Integrate vision model for contextual classification.
- Store parsed output in structured JSON format.

**Step 2: Develop Narrative Structuring Engine**
- Implement recursive event detection.
- Apply three-act storytelling principles.

**Step 3: Connect System State to Storytelling**
- Link session memory with narrative persistence.
- Identify cross-session patterns & residual markers.

**Step 4: Test & Optimize for Real-World Scenarios**
- Validate generated narratives across multiple session states.
- Implement manual tuning parameters for custom storytelling.

## Final Outcome:
OLCA will evolve into an adaptive storytelling CLI, capable of interpreting screenshots, structuring narratives, and embedding recursive system intelligence.

## Next Steps:
- Implement Ollama-based vision analysis.
- Develop ontology-driven narrative generation.
- Validate story coherence across multiple screenshots.

This feature enables OLCA to bridge structured execution memory with generative storytelling, turning system interactions into meaningful narratives.
