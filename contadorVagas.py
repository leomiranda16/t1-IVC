import cv2
# Lista pra guardar as coordenadas
coords = []
clicks = []

# Função que captura os cliques do mouse
def clique(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicks.append((x, y))
        print(f'Ponto {len(clicks)}: ({x}, {y})')

        # Desenha um pontinho
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Imagem", img)

        # Se tiver 4 pontos, salva como uma vaga (retângulo)
        if len(clicks) == 4:
            coords.append(clicks.copy())
            print(f"Vaga salva: {clicks}")
            clicks.clear()

# Carrega a imagem
img = cv2.imread(r"C:\Users\leomi\OneDrive - PUCRS - BR\PUCRS\5° Semestre\Introdução á Visão Computacional\T1\Captura de tela 2025-05-04 150930.png")
cv2.imshow("Imagem", img)
cv2.setMouseCallback("Imagem", clique)

print("Clique em 4 cantos de cada vaga. Pressione ESC pra sair.")

while True:
    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break

cv2.destroyAllWindows()

# Mostra todas as coordenadas capturadas
print("Coordenadas das vagas:")
for i, vaga in enumerate(coords):
    print(f"Vaga {i+1}: {vaga}")
