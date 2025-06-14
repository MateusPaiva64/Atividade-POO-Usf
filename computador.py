class Computador:
    def __init__(self, marca, memoria_ram, armazenamento, ligado=False):
        self.__marca = marca
        self.__memoria_ram = memoria_ram  # em GB
        self.__armazenamento = armazenamento  # em GB
        self.__ligado = ligado

    # Getters
    def get_marca(self):
        return self.__marca

    def get_memoria_ram(self):
        return self.__memoria_ram

    def get_armazenamento(self):
        return self.__armazenamento

    def is_ligado(self):
        return self.__ligado

    # Setters
    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_memoria_ram(self, nova_memoria_ram):
        self.__memoria_ram = nova_memoria_ram

    def set_armazenamento(self, novo_armazenamento):
        self.__armazenamento = novo_armazenamento

    # Método adicional: ligar computador
    def ligar_computador(self):
        if not self.__ligado:
            self.__ligado = True
            return f"O computador {self.__marca} foi ligado com sucesso!"
        else:
            return f"O computador {self.__marca} já está ligado."
