# Comparison Plan

Depth Pro should be compared against models that represent different assumptions about monocular depth.

## Models to Compare

| Model | Role |
| --- | --- |
| Depth Anything V2 | Strong relative-depth foundation baseline |
| UniDepth | Universal metric depth and camera-aware prediction |
| Metric3D | Zero-shot metric depth and normal estimation |
| Marigold | Diffusion-prior depth with strong in-the-wild visual quality |
| GeoWizard | Diffusion-prior depth and normal estimation |

## Comparison Axes

- Relative depth structure.
- Metric scale accuracy.
- Boundary sharpness.
- Focal length behavior.
- Robustness to unknown cameras.
- Speed and VRAM.
- License and deployment constraints.

## Dataset Buckets

- Indoor: NYUv2-like rooms, ScanNet-like spaces.
- Outdoor: KITTI-like roads, parks, buildings.
- In-the-wild: phone images, web images, unusual crops.
- Fine-boundary: fences, plants, furniture, hair, wires.

## Expected Outcome

The goal is not to crown one universal winner. The goal is to understand when Depth Pro is the best choice and when another model is more appropriate.

