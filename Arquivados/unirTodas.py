from PIL import Image
import os
import re

pasta_imagens = "semSobras"
pasta_saida = "paginas_combinadas"

os.makedirs(pasta_saida, exist_ok=True)

# Função para extrair o número da página
def extrair_numero(nome_arquivo):
    match = re.search(r'pagina_enem_(\d+)_', nome_arquivo)
    if match:
        return int(match.group(1))
    return 0

# Coletar todas as imagens
imagens_esquerda = []
imagens_direita = []

for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        if 'esquerda' in nome_arquivo.lower():
            imagens_esquerda.append(nome_arquivo)
        elif 'direita' in nome_arquivo.lower():
            imagens_direita.append(nome_arquivo)

# Ordenar as imagens pelo número da página
imagens_esquerda.sort(key=extrair_numero)
imagens_direita.sort(key=extrair_numero)

# Verificar se temos o mesmo número de páginas esquerda e direita
if len(imagens_esquerda) != len(imagens_direita):
    print(f"Aviso: Número diferente de páginas esquerda ({len(imagens_esquerda)}) e direita ({len(imagens_direita)})")

# Combinar as páginas na ordem: direita, esquerda, direita, esquerda...
imagens_combinadas = []

for i in range(min(len(imagens_esquerda), len(imagens_direita))):
    # Adicionar direita primeiro
    imagens_combinadas.append(imagens_direita[i])
    # Adicionar esquerda depois
    imagens_combinadas.append(imagens_esquerda[i])

# Se houver páginas extras de algum tipo, adicionar no final
if len(imagens_esquerda) > len(imagens_direita):
    imagens_combinadas.extend(imagens_esquerda[len(imagens_direita):])
elif len(imagens_direita) > len(imagens_esquerda):
    imagens_combinadas.extend(imagens_direita[len(imagens_esquerda):])

# Combinar todas as imagens verticalmente
imagens_abertas = []
largura_maxima = 0
altura_total = 0

for nome_arquivo in imagens_combinadas:
    caminho_imagem = os.path.join(pasta_imagens, nome_arquivo)
    img = Image.open(caminho_imagem)
    imagens_abertas.append(img)
    
    # Atualizar dimensões máximas
    largura_maxima = max(largura_maxima, img.width)
    altura_total += img.height

# Criar imagem final
imagem_final = Image.new('RGB', (largura_maxima, altura_total))

# Colar as imagens uma em cima da outra
y_offset = 0
for img in imagens_abertas:
    # Centralizar horizontalmente se necessário
    x_offset = (largura_maxima - img.width) // 2
    imagem_final.paste(img, (x_offset, y_offset))
    y_offset += img.height

# Salvar a imagem combinada
caminho_final = os.path.join(pasta_saida, "enem_completo.png")
imagem_final.save(caminho_final)

print(f"Combinação concluída! {len(imagens_combinadas)} páginas combinadas.")
print(f"Imagem salva como: {caminho_final}")

# Mostrar a ordem das páginas combinadas
print("\nOrdem das páginas combinadas:")
for i, nome_arquivo in enumerate(imagens_combinadas, 1):
    print(f"{i}. {nome_arquivo}")