# Depth Pro Research

A focused research and evaluation wrapper around Apple's Depth Pro for sharp zero-shot metric monocular depth estimation.

Official upstream:

- Paper: [Depth Pro: Sharp Monocular Metric Depth in Less Than a Second](https://arxiv.org/abs/2410.02073)
- Apple research page: [machinelearning.apple.com/research/depth-pro](https://machinelearning.apple.com/research/depth-pro)
- Official code: [apple/ml-depth-pro](https://github.com/apple/ml-depth-pro)

## What I Changed

This repository is not a mirror of the official Apple implementation. Instead, it adds a research-oriented layer around the original project:

- Reframed Depth Pro from a spatial intelligence perspective.
- Added a reproducible evaluation manifest format for future experiments.
- Added boundary-quality and focal-length analysis notes.
- Added a comparison plan against Depth Anything V2, UniDepth, Metric3D, and Marigold.
- Added lightweight validation scripts so experiment metadata stays clean.
- Separated official baseline notes from my own planned extensions.

## Why Depth Pro

Depth Pro is useful for spatial intelligence because it predicts metric depth from a single RGB image without requiring camera intrinsics. This matters for real-world images where the camera model is unknown, missing, or unreliable.

Key capabilities to study:

- Zero-shot metric depth in meters.
- High-resolution depth maps with sharp boundaries.
- Focal length prediction from a single image.
- Boundary-aware evaluation metrics.
- Fast inference relative to many high-quality dense prediction systems.

## Research Questions

| Question | Why It Matters |
| --- | --- |
| How reliable is metric scale without known intrinsics? | Affects robotics, AR, reconstruction, and measurement |
| Where does Depth Pro beat relative-depth foundation models? | Separates metric value from visual plausibility |
| How sharp are object boundaries and thin structures? | Important for scene parsing and 3D reconstruction |
| How does focal length prediction behave on web images? | Tests robustness under unknown cameras |
| What failure cases appear in indoor, outdoor, and in-the-wild images? | Guides future project improvements |

## Repository Structure

```text
.
├── README.md
├── configs/
│   └── eval_manifest.example.json
├── docs/
│   └── official-baseline.md
├── notes/
│   ├── boundary-and-focal-length.md
│   └── comparison-plan.md
├── scripts/
│   └── validate_manifest.py
└── LICENSE
```

## Planned Workflow

1. Install the official `apple/ml-depth-pro` implementation in a separate environment.
2. Select a small but diverse image set: indoor, outdoor, fine structures, unknown-camera web images.
3. Run Depth Pro and store output metadata using `configs/eval_manifest.example.json` as the template.
4. Compare against Depth Anything V2, UniDepth, Metric3D, and Marigold.
5. Summarize strengths, failures, and use-case recommendations.

## Current Status

- Research framing: done
- Official baseline summary: done
- Evaluation manifest: done
- Metadata validation script: done
- Model execution scripts: planned
- Qualitative gallery: planned
- Cross-model benchmark: planned

## Disclaimer

This repository is an independent research wrapper. It does not redistribute Depth Pro source code, pretrained weights, or Apple-owned assets. Please follow the official repository and license terms when using the upstream model.

