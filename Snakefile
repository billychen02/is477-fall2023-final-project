rule prepare:
  output:
    "data\wdbc.data",
    "data\wdbc.names"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input:
    "data\wdbc.data"
  output:
    "profiling/report.html"
  shell:
    "python scripts/profile.py"

rule analyze:
  input:
    "data\wdbc.data"
  output:
    "results/BM_comparison.png",
    "results/feature_importance.png",
    "summary_stats.csv",
    "wisconsin_breast_cancer_analysis.txt"
  shell:
    "python scripts/analyze.py"