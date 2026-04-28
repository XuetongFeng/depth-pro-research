# Boundary and Focal-Length Notes

Depth Pro is especially interesting because it combines metric depth, sharp boundaries, and focal length estimation from a single image.

## Boundary Quality

Boundary quality matters when depth is used for:

- Object-aware scene parsing.
- 3D reconstruction from a single image.
- View synthesis and image editing.
- Robotics manipulation around object edges.
- AR occlusion and placement.

Depth maps can look globally plausible while still failing at thin structures. For this project, boundary analysis should prioritize:

- Chair legs and table edges.
- Railings and fences.
- Plants and tree branches.
- Human hair and clothing contours.
- Reflective or transparent boundaries.

## Focal Length

Focal length prediction matters because metric depth from a single image is tightly connected to camera geometry.

Questions to test:

- Does focal length prediction remain stable across resized images?
- Does EXIF metadata agree with the predicted focal length when available?
- Are errors larger for wide-angle, cropped, or social-media images?
- Does focal length error correlate with metric depth error?

## Suggested Output Fields

For every evaluated image, store:

- Image source and license.
- Original resolution.
- Whether EXIF focal length is available.
- Predicted focal length.
- Qualitative boundary rating.
- Observed metric-scale issues.
- Notes on failure cases.

