file_path = r"C:\WorkDirve\BKP\Projects\Python\SQL Spliter\qu.txt"

try:
    # Read the file
    with open(file_path, "r", encoding="utf-8-sig") as file:
        content = file.read()

    # Find and replace the specified text
    search_text = ",\n ;\nGO"
    updated_content = content.replace(search_text,";\nGO")

    # Save changes to the same file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    # Display results
    replacements = content.count(search_text)
    print(f"Completed successfully!")
    print(f"Replacements made: {replacements}")
    print(f"Updated file: {file_path}")

except FileNotFoundError:
    print(f"Error: File not found: {file_path}")

except Exception as e:
    print(f"Error: {e}")