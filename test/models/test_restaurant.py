from src.models.restaurant import Restaurant
class TestRestaurant:

    def test_describe_restaurant(self):
        restaurant = Restaurant("Estação do Sabor", "Comida Mineira")
        number_served = 10
        expected = 'Esse restaurante chama Estação do Sabor e serve Comida Mineira.' \
                   '\n\tEsse restaurante está servindo 10 consumidores desde que está aberto.'
        result = restaurant.describe_restaurant(number_served)
        assert expected == result

    def test_open_restaurant(self):
        restaurant = Restaurant("Estação do Sabor", "Comida Mineira")
        number_served = 0
        expected = "Estação do Sabor agora está aberto!"
        result = restaurant.open_restaurant(number_served=number_served)
        assert expected == result

    def test_restaurant_already_open(self):
        restaurant = Restaurant("Estação do Sabor", "Comida Mineira")
        number_served = 5
        expected = "Estação do Sabor já está aberto!"
        result = restaurant.open_restaurant(number_served=number_served)
        assert expected == result

    def test_close_restaurant(self):
        restaurant = Restaurant("Estação do Sabor", "Comida Mineira")
        number_served = 10
        expected = "Estação do Sabor agora está fechado!"
        result = restaurant.close_restaurant(number_served=number_served)
        assert expected == result

    def test_restaurant_already_closed(self):
        restaurant = Restaurant("Estação do Sabor", "Comida Mineira")
        number_served = 0
        expected = "Estação do Sabor já está fechado!"
        result = restaurant.close_restaurant(number_served=number_served)
        assert expected == result

    def test_set_number_served(self):
        restaurant = Restaurant("Estação do Sabor", "Comida Mineira")
        total_customers = 15
        expected = "Estação do Sabor já serviu 15 clientes até o momento!"
        result = restaurant.set_number_served(total_customers=total_customers)
        assert expected == result

    def test_increment_number_served(self):
        restaurant = Restaurant("Estação do Sabor", "Comida Mineira")
        more_customers = 20
        expected = "Estação do Sabor já atendeu 20 clientes novos!"
        result = restaurant.increment_number_served(more_customers=more_customers)
        assert expected == result
