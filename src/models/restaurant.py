class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        # Removido o .title() do restaurant_name
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self, number_served):
        """Imprima uma descrição simples da instância do restaurante."""
        # Corrigido para retornar os valores ao invés de imprimir
        # Corrigido para retornar o nome do restaurante e para retornar o número informado de clientes atendidos
        msg1 = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}."
        msg2 = f"Esse restaurante está servindo {number_served} consumidores desde que está aberto."
        return f"{msg1}\n\t{msg2}"

    def open_restaurant(self, number_served):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        # Alterado a lógica para verificar se o restaurante já está aberto
        if not self.open and number_served == 0:
            self.open = True
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self, number_served):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        # Alterado a lógica para verificar se o restaurante já está fechado
        if not self.open and number_served > 0:
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        #  Alterado a lógica e a mensagem
        self.number_served = total_customers
        return f"{self.restaurant_name} já serviu {self.number_served} clientes até o momento!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        #  Alterado a lógica e a mensagem
        self.number_served = more_customers
        return f"{self.restaurant_name} já atendeu {self.number_served} clientes novos!"
