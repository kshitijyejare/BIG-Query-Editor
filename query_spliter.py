file_path = r"C:\WorkDirve\BKP\Projects\Python\SQL Spliter\qu.txt"

insert_text = """ ;
GO

-- Insert sample data
INSERT INTO dbo.fact_forecast_monthly
(
    [date],
    division,
    category,
    product_code,
    product,
    market,
    platform,
    channel,
    customer_code,
    customer_name,
    forecast_quantity
)
VALUES
"""

lines_per_block = 900

# Read the original file
with open(file_path, "r", encoding="utf-8-sig") as file:
    lines = file.readlines()

# Insert SQL text after every 900 lines
updated_lines = []

for i, line in enumerate(lines, start=1):
    updated_lines.append(line)

    if i % lines_per_block == 0 and i < len(lines):
        updated_lines.append(insert_text + "\n")

# Save changes back to the same file
with open(file_path, "w", encoding="utf-8") as file:
    file.writelines(updated_lines)

print(f"Done! Updated file: {file_path}")
print(f"Original line count: {len(lines)}")
print(f"SQL text inserted: {(len(lines) - 1) // lines_per_block} times")