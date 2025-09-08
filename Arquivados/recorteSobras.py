from PIL import Image
import os

pasta_imagens = "metades"
pasta_saida = "semSobras"

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith((".png", ".jpg", ".jpeg")):
        caminho_entrada = os.path.join(pasta_imagens, nome_arquivo)
        imagem = Image.open(caminho_entrada)

        largura, altura = imagem.size
        
        if nome_arquivo.lower().endswith("esquerda.png"):
            caixa_corte = (0, 0, largura - 25, altura)
            imagem_cortada = imagem.crop(caixa_corte)
            
        elif nome_arquivo.lower().endswith("direita.png"):
            caixa_corte = (25, 0, largura, altura)
            imagem_cortada = imagem.crop(caixa_corte)
        
        else:
            imagem_cortada = imagem

        caminho_saida = os.path.join(pasta_saida, nome_arquivo)
        imagem_cortada.save(caminho_saida)

print("Recorte das bordas laterais concluído.")