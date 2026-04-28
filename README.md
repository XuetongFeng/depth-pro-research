# Depth Pro Research

This repository is my research-oriented copy of Apple's **Depth Pro** project, extended for spatial intelligence and monocular metric depth study.

Upstream:

- Paper: [Depth Pro: Sharp Monocular Metric Depth in Less Than a Second](https://arxiv.org/abs/2410.02073)
- Apple research page: [machinelearning.apple.com/research/depth-pro](https://machinelearning.apple.com/research/depth-pro)
- Official repository: [apple/ml-depth-pro](https://github.com/apple/ml-depth-pro)
- Upstream snapshot used here: `apple/ml-depth-pro` commit `9efe5c1`

## What I Added

The original Depth Pro repository provides the model implementation, setup flow, inference API, pretrained checkpoint script, and boundary metric utilities. On top of that, I added:

- `docs/official-baseline.md`: a compact summary of the official implementation and what belongs to upstream.
- `notes/boundary-and-focal-length.md`: my notes on why boundary quality and focal length prediction matter for spatial intelligence.
- `notes/comparison-plan.md`: a comparison plan against Depth Anything V2, UniDepth, Metric3D, Marigold, and GeoWizard.
- `configs/eval_manifest.example.json`: a small manifest format for tracking evaluation images and outputs.
- `scripts/validate_manifest.py`: a validation script to keep evaluation metadata clean.
- `UPSTREAM_README.md`: the original upstream README preserved for reference.

## Why This Project

Depth Pro is especially relevant to spatial intelligence because it predicts **metric depth** from a single RGB image without requiring known camera intrinsics. This makes it useful for real-world images where camera metadata is missing, noisy, or unavailable.

My focus in this copy is not only to run the model, but to study:

- when metric depth is reliable without camera intrinsics;
- how sharp the predicted depth boundaries are;
- how focal length prediction behaves on unknown-camera images;
- where Depth Pro differs from Depth Anything V2, UniDepth, Metric3D, and diffusion-based geometry models;
- how monocular depth can support 3D reconstruction, AR, robotics, and scene understanding.

## Repository Structure

```text
.
├── src/depth_pro/                 # Upstream Depth Pro package
├── eval/                          # Upstream evaluation utilities
├── data/                          # Upstream example assets
├── configs/                       # My evaluation manifest template
├── docs/                          # My baseline documentation
├── notes/                         # My research notes
├── scripts/                       # My lightweight validation scripts
├── UPSTREAM_README.md             # Original upstream README
├── pyproject.toml                 # Upstream package config
└── get_pretrained_models.sh       # Upstream checkpoint download script
```

## Getting Started

The upstream setup is preserved. In short:

```bash
conda create -n depth-pro -y python=3.9
conda activate depth-pro
pip install -e .
source get_pretrained_models.sh
```

Run a single-image prediction:

```bash
depth-pro-run -i ./data/example.jpg
```

For complete official instructions, see [UPSTREAM_README.md](UPSTREAM_README.md).

## Validate My Evaluation Manifest

```bash
python3 scripts/validate_manifest.py
```

Expected output:

```text
Validated 2 image entries.
```

## Current Status

- Upstream code copied: done
- Upstream README preserved: done
- Research framing: done
- Evaluation manifest: done
- Metadata validation: done
- Local model execution: planned
- Qualitative comparison gallery: planned
- Cross-model benchmark: planned

## License and Attribution

The upstream Depth Pro code and model terms are governed by Apple's original license in [LICENSE](LICENSE). This repository preserves upstream attribution and includes my additional research notes and evaluation scaffolding.

This is an independent research copy and is not affiliated with Apple.
