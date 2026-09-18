# Public prototype code

These scripts are deliberately small.

They show two pieces of the architecture that can be made transparent without publishing the whole private prototype history:

1. **SDS evidence extraction** - finding environmental H-codes and aquatic toxicity endpoints in text.
2. **Deterministic screening risk** - calculating a PEC, PNEC and RQ from explicit user-supplied assumptions.

The code does not reproduce all historical ChemCodex scoring logic. That is intentional. Several older thresholds were experimental or too broadly described as regulatory rules.

Nothing in this folder is an approved regulatory method.

## Run the example

From the repository root:

```bash
python prototype_code/demo.py
```

The example uses synthetic data only.
