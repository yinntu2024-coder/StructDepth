# StructDepth — paper-aligned reproduction patch

这是针对用户提供的 StructDepth 原始代码包与论文逐项核对后生成的**论文一致性与稳定性修复补丁**。

> 当前仓库采用“原始代码 + 精确补丁”的交付方式，而不是重新上传二进制 ZIP。原因是当前 ChatGPT GitHub 连接器只适合写入 UTF-8 文本文件。补丁本身已无损压缩、Base64 分片并提交到 `patch_parts/`，可确定性地恢复为原始 `.diff`。

## 一键恢复补丁

```bash
 git clone https://github.com/yinntu2024-coder/StructDepth.git StructDepth-fix
 cd StructDepth-fix
 python rebuild_patch.py
```

成功后会生成：

```text
StructDepth_patch_from_uploaded.diff
```

其 SHA256 必须为：

```text
df125ef3acf7b429785df18a84e075b95f844ced3852afce243b9068abc648af
```

## 应用到你最初上传的 StructDepth 代码

进入**原始代码的 `StructDepth/` 根目录**后执行：

```bash
patch --batch -p5 < /path/to/StructDepth-fix/StructDepth_patch_from_uploaded.diff
```

该命令已经针对本次上传的原始代码副本进行 `--dry-run` 和实际应用验证；应用后的内容与审查后的修复工作树逐文件一致。

如果在 Windows/Anaconda Prompt 下没有 `patch` 命令，推荐在 Git Bash 或 WSL 中执行上述命令。

## 本补丁涉及的主要文件

- `networks/StructDepth.py`
- `networks/mamba_encoder.py`
- `networks/csm_triton.py`
- `networks/csms6s.py`
- `trainer.py`
- `layers.py`
- `options.py`
- `train.py`
- `evaluate_kitti.py`
- `evaluate_make3d.py`
- `evaluate_pose.py`
- `export_gt_depth.py`
- `preflight.py`
- `requirements.txt`
- `tests/test_smoke.py`
- `args/structdepth_kitti_640x192_paper.txt`
- `REVIEW.md`
- `VALIDATION.md`

## 关键修复方向

- 对齐论文中的 STRU / SEE / SGSR / STIM / GCI 数据流与监督位置。
- 恢复 GCI 的 Sobel edge-aware calibration 分支。
- 修正 STIM 与 `d3` 深监督的执行顺序。
- 统一 `Project3D` 与 `grid_sample` 的 `align_corners` 几何约定。
- 按论文四尺度目标恢复 smoothness 权重逻辑。
- 修复 CPU/GPU device、dynamic batch、checkpoint、配置解析与评测依赖问题。
- 对 selective-scan / Triton 缺失环境提供可执行兼容路径。
- 增加 `preflight.py` 与 smoke tests，降低长时间训练后才暴露错误的风险。

## 校验信息

原始修复补丁：

```text
SHA256  df125ef3acf7b429785df18a84e075b95f844ced3852afce243b9068abc648af
```

本地审查时生成的完整修复 ZIP：

```text
SHA256  d5f7dfb4f19a5c79f2c4f4e296e325dc7b68da38436acaeecb21d0e912976b41
```

注意：论文中的最终 KITTI 指标仍必须在完整数据集、正确 VMamba 预训练权重和论文训练协议下重新训练验证；本仓库不把“代码链路验证通过”等同于“已经复现论文最终数值”。
