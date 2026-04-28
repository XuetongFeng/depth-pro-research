# Official Depth Pro Baseline

This note summarizes the official Depth Pro project so future changes are clearly separated from upstream work.

## Upstream

- Official repository: <https://github.com/apple/ml-depth-pro>
- Research page: <https://machinelearning.apple.com/research/depth-pro>
- Paper: <https://arxiv.org/abs/2410.02073>

## Official Capabilities

The official project accompanies the Depth Pro paper. It provides:

- A reference implementation.
- Pretrained checkpoint download script.
- Command-line inference through `depth-pro-run`.
- Python inference API.
- Metric depth output in meters.
- Focal length prediction in pixels.
- Boundary metrics under the official evaluation utilities.

## Important Upstream Notes

- The official repository states that its released model is a retrained reference implementation and may not exactly match the reported paper model.
- The official implementation has its own license terms.
- This repository does not copy the official source code or weights.

## My Additions in This Repository

- Clearer research positioning for spatial intelligence.
- Experiment metadata format.
- Boundary and focal-length evaluation plan.
- Comparison plan against other SOTA monocular depth systems.
- Validation script for experiment manifests.

