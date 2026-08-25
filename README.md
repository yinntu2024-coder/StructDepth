# StructDepth — paper-aligned reproduction

This repository hosts the paper-aligned and stability-fixed StructDepth reproduction prepared from the supplied manuscript and source archive.

The corrected full source package is committed as `StructDepth_fixed.zip`. It includes the implementation, paper-aligned training configuration, preflight checks, smoke tests, `REVIEW.md`, and `VALIDATION.md`.

Key fixes include paper-consistent STRU/SEE/SGSR/STIM/GCI wiring, Sobel-based GCI calibration, STIM-to-d3 supervision order, projection/grid-sampling coordinate consistency, four-scale loss weighting, device-safe execution, strict checkpoint/config validation, and reproducibility safeguards.
