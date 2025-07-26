import polars as pl

# Define input and output paths
input_path = "Prestaciones de salud asociadas a los asegurados con Diabetes Mellitus.csv"
output_path = "Prestaciones_de_salud_asociadas_a_los_asegurados_con_Diabetes_Mellitus.parquet"

# Define schema fixes
schema_fix = {
    "CODPREST": pl.Utf8,
    "IDCIE10": pl.Utf8,
}

# Read the CSV file with specified parameters
df = pl.read_csv(
    input_path,
    separator=",",
    encoding="latin1",
    schema_overrides=schema_fix,
    null_values=["", "S.I.", "S0001"],
    truncate_ragged_lines=True,
    ignore_errors=True,
    try_parse_dates=True
)

# Write to Parquet format
df.write_parquet(output_path)

print(f"Successfully converted CSV to Parquet: {output_path}")