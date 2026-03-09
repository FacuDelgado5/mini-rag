from src.rag_pipeline import run_rag

while True:
    try:
        pdf_count = int(input("\n¿Cuántos PDFs quiere cargar? (1-3): "))

        if 1 <= pdf_count <= 3:
            break
        else:
            print("\nSolo puede cargar entre 1 y 3 PDFs. Intente nuevamente.")
    except ValueError:
        print("\nError: Ingrese un número válido entre 1 y 3.")

pdf_paths = []

for i in range(pdf_count):
    pdf_path = input(f"Ingrese la ruta del PDF {i + 1}: ").strip()
    pdf_paths.append(pdf_path)

while True:
    query = input("\nPregunta: ").strip()

    if query:
        break
    else:
        print("\nError: Debes escribir una pregunta.")

answer = run_rag(pdf_paths, query)

print("\nRespuesta:")
print(answer)