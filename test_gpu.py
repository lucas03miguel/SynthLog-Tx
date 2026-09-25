
import torch

# Verifica se o PyTorch consegue comunicar com a API CUDA
print("CUDA Disponível:", torch.cuda.is_available())

# Devolve o nome exato da placa gráfica detetada
if torch.cuda.is_available():
    print("Nome da GPU:", torch.cuda.get_device_name(0))
    print("Memória Total (GB):", round(torch.cuda.get_device_properties(0).total_memory / 1e9, 2))
else:
    print("A GPU não foi detetada. O treino ocorrerá no CPU (i5).")