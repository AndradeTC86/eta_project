from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        # Corrigido para retornar os valores ao invés de imprimir
        if self.flavors:
            msg = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                msg = (f"{msg}\n\t-{flavor}")
            return msg
        else:
            return "Estamos sem estoque atualmente!"


    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        # Corrigido para retornar os valores ao invés de imprimir
        # Adicionado validação para verificar se o nome foi passado
        if flavor is not None:
            if self.flavors:
                if flavor in self.flavors:
                    return f"Temos no momento {flavor}!"
                else:
                    return f"Não temos no momento {flavor}!"
            else:
                return "Estamos sem estoque atualmente!"
        return "Sabor não foi informado"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        # Corrigido para retornar os valores ao invés de imprimir
        # Adicionado validação para verificar se o nome está em branco
        # Removida a mensagem de falta de estoque
        if flavor is not None:
            if self.flavors:
                if flavor in self.flavors:
                    return "\nSabor já disponivel!"
                else:
                    self.flavors.append(flavor)
                    return f"{flavor} adicionado ao estoque!"
        return "Sabor não foi informado"
