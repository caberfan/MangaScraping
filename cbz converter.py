from pathlib import Path
import zipfile

# Current working directory
root = Path.cwd()

for folder in root.iterdir():
    if not folder.is_dir():
        continue

    cbz_path = folder.with_suffix(".cbz")

    print(f"Creating {cbz_path.name}...")

    with zipfile.ZipFile(cbz_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file in folder.rglob("*"):
            if file.is_file():
                # Preserve folder structure inside the CBZ
                zf.write(file, arcname=file.relative_to(folder))

print("Done!")