import threading
import requests

# Função para baixar uma imagem
def baixar_imagem(url, nome_arquivo):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para status de erro HTTP
        with open(nome_arquivo, 'wb') as file:
            file.write(response.content)
        print(f"{nome_arquivo} baixado com sucesso.")
    except requests.exceptions.RequestException as e:
        print(f"Falha ao baixar {nome_arquivo}: {e}")

# Função principal
def main():
    # URLs das imagens que serão baixadas
    urls = [
        "https://www.example.com/imagem1.jpg",
        "https://www.example.com/imagem2.jpg",
        "https://www.example.com/imagem3.jpg",
        "https://www.example.com/imagem4.jpg"
    ]
    
    # Nomes dos arquivos para salvar as imagens
    nomes_arquivos = ["imagem1.jpg", "imagem2.jpg", "imagem3.jpg", "imagem4.jpg"]
    
    # Lista para armazenar as threads
    threads = []
    
    # Criando e iniciando as threads
    for i in range(len(urls)):
        thread = threading.Thread(target=baixar_imagem, args=(urls[i], nomes_arquivos[i]))
        threads.append(thread)
        thread.start()
    
    # Aguardando todas as threads terminarem
    for thread in threads:
        thread.join()
    
    print("Downloads concluídos.")

if __name__ == "__main__":
    main()
