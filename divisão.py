from pdf2image import convert_from_path
import os

pdf_path = "enem2024.pdf"
output_folder = "imagens"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

    resolucao_dpi = 300

    print("convertendo '(pdf_path)' para imagens com (resolucao_dpi) DPI...")

    try:
        images =convert_from_path(
            pdf_path,
            dpi = resolucao_dpi,
            output_folder = output_folder,
            fmt = "png",
            paths_only = False,
        );

        for i, image in enumerat(images):
            images_filename = os.path.join(output_folder, f"pagina_enem_{i+1}.png")
            image.save(images_filename)
            print("Página {i+1} salva como '{images_filename}'")

            print("\nConversão concluída! AS imagens foram salvas na pasta '{output_folder}'.")

            except Exception as e:
                print(f"Ocorreu um erro durante a conversão:{e}")
                print("Verifique se o Poppler está instalado corretamente e se o caminho do PDF está correto.")